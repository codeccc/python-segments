# encoding=utf-8
import re

from bs4 import BeautifulSoup
from urllib import request
import codecs
from mylog import MyLog as mylog


class MovieItem(object):
    movieName = None
    movieScore = None
    movieStarring = None
    movieThumb = None


class GetMovie(object):
    def __init__(self):
        self.urlBase = 'http://dianying.2345.com/list/-------1.html'
        self.log = mylog()
        self.pages = self.getPages()  # 获取所有页数
        self.urls = []
        self.items = []
        self.getUrls(self.pages)  # 获取所有页数对应的链接
        self.spider(self.urls)  # 根据链接进爬取
        self.pipelines(self.items)  # 根据页数进行保存

    def getPages(self):
        self.log.info('开始获取页数')
        htmlContent = self.getResponseContent(self.urlBase)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find('div', attrs={'class': 'v_page'})
        subTags = tag.find_all('a')
        self.log.info('获取页数成功')
        return int(subTags[-2].get_text())
        # return 10

    def getResponseContent(self, url):
        try:
            conn = request.Request(url, headers={'User-Agent': \
                                                     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
            response = request.urlopen(conn)
        except:
            self.log.error('Python 返回 URL : %s 数据失败' % url)
        else:
            self.log.info('Python 返回 URL : %s 数据成功' % url)
            return str(response.read().decode('GB18030'))

    def getUrls(self, pages):
        self.urls.clear()
        url_tmp = 'http://dianying.2345.com/list/-------{}.html'
        for i in range(1, pages + 1):
            url = url_tmp.format(i)
            self.urls.append(url)
            self.log.info('添加URL: %s 到URLS列表' % url)

    def spider(self, urls):
        num = 0
        for url in urls:
            num += 1
            htmlContent = self.getResponseContent(url)
            print(url)
            soup = BeautifulSoup(htmlContent, 'html.parser')
            anchorTag = soup.find('ul', attrs={'class': 'v_picTxt pic180_240 clearfix'})
            tags = anchorTag.find_all('li')

            for tag in tags:
                if tag.find('div', attrs={'class': 'ivyAuto'}):
                    continue
                item = MovieItem()
                item.movieName = tag.find('em', attrs={
                    'class': 'emTit'}).a.get_text()
                item.movieScore = tag.find('span',
                                           attrs={'class': 'pRightBottom'}).em.get_text().replace(
                    '分', '')
                ems = tag.find('span', attrs={'class': 'sDes'}).find_all('em')
                item.movieStarring = []
                for em in ems:
                    item.movieStarring.append(em.a.get_text().replace('  ', ''))
                print(tag.div.img.attrs)
                item.movieThumb = 'http:' + tag.div.img['data-src']
                self.d_image(item.movieThumb, item.movieName)
                self.items.append(item)
                self.log.info('获取视频成功,视频信息如下:\n电影名称:\t%s\n评分:\t%s\n封面图:\t%s\n主演:\t%s' % (
                    item.movieName, item.movieScore, item.movieThumb, item.movieStarring))
            print('当前页数: ', num)

    def pipelines(self, items):
        fileName = '热门电影.txt'
        with codecs.open(fileName, 'w', 'utf-8') as fp:
            for item in items:
                fp.write('%s \t %s \t %s \t %s \r\n' % (
                    item.movieName, item.movieScore, item.movieThumb, item.movieStarring))
                self.log.info('电影名为: <<%s>>已成功存入文件:%s...' % (item.movieName, fileName))

    def d_image(self, imgurl, fname):

        import os
        root_dir = './image/'
        if not os.path.exists():
            os.mkdir(root_dir)

        suffix = re.search('(.png|.jpg|.jpeg)', imgurl.lower()).group()
        request.urlretrieve(imgurl, root_dir + fname + suffix)


if __name__ == '__main__':
    GM = GetMovie()
