## python-segments

日常编写/收集一些通用的代码片段/文档



### 文档

[Scrapy爬虫框架入门之初识Scrapy](https://github.com/codeccc/python-segments/blob/master/docs/Scrapy爬虫框架入门之初识Scrapy.md)



### 代码片段

#### 1. 遍历文件夹得到目录下所有文件 [file_iter.py](https://github.com/codeccc/python-segments/blob/master/file/file_iter.py)

代码如下: `your_path`  为你要扫描的文件夹路径. 

```python
# encoding=utf-8

import os
from prettyprinter import pprint

your_path=r'C:\Users\Administrator\Pictures' # 这里定义你要遍历的路径

def read_file(f_path):
    if os.path.isdir(f_path): #判断是否为文件夹
        f_list = os.listdir(f_path) # 获得目录下所有文件
        for file in f_list:
            read_file(f_path + '\\' + file) # 递归再进行读取
    else:
        with open(f_path) as f:
            pprint(f.name) # 打印文件路径

#开始遍历读取
read_file(your_path)

```

#### 2. 常见的UserAgent大全  [user_agents.py](https://github.com/codeccc/python-segments/file/fuser_agents.py)

代码如下:

```python
#!/usr/bin/env python
#-*- coding: utf-8 -*-

pcUserAgent = {
    "safari 5.1 – MAC":"User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "safari 5.1 – Windows":"User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "IE 9.0":"User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
    "IE 8.0":"User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "IE 7.0":"User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "IE 6.0":"User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Firefox 4.0.1 – MAC":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Firefox 4.0.1 – Windows":"User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera 11.11 – MAC":"User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera 11.11 – Windows":"User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Chrome 17.0 – MAC":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Maxthon":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Tencent TT":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "The World 2.x":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "The World 3.x":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "sogou 1.x":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "360":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Avant":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Green Browser":"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
}

mobileUserAgent = {
    "iOS 4.33 – iPhone":"User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "iOS 4.33 – iPod Touch":"User-Agent:Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "iOS 4.33 – iPad":"User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Android N1":"User-Agent: Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Android QQ":"User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Android Opera ":"User-Agent: Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Android Pad Moto Xoom":"User-Agent: Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "BlackBerry":"User-Agent: Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "WebOS HP Touchpad":"User-Agent: Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Nokia N97":"User-Agent: Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Windows Phone Mango":"User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UC":"User-Agent: UCWEB7.0.2.37/28/999",
    "UC standard":"User-Agent: NOKIA5700/ UCWEB7.0.2.37/28/999",
    "UCOpenwave":"User-Agent: Openwave/ UCWEB7.0.2.37/28/999",
    "UC Opera":"User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
}
```



### 项目实战

#### 实战一 爬取2345影视电影信息

**爬取网址:**  http://dianying.2345.com/list/-------1.html

##### 需求分析

爬取该页面下的电影信息, 包含电影名称, 电影评分, 主演 及电影缩略图, 将全部页数下的电影保存到 热门电影.txt   ,缩略图保存到文件夹 image 下

![网站截图](./imgs/1.jpg)



##### 使用技术分析

 使用urllib访问链接获取源代码并保存图片,使用BeatifulSoup解析标签,使用正则表达式提取关键字,使用logging记录操作日志

##### **爬取结果:**

```
热门电影.txt

追龙Ⅱ 	 8.9 	 http://imgwx3.2345.com/dypcimg/img/4/67/s203534.jpg?1558957030 	 ['梁家辉\xa0\xa0', '古天乐\xa0\xa0'] 
流浪地球 	 9.6 	 http://imgwx4.2345.com/dypcimg/img/0/67/s201366.jpg?1556617765 	 ['屈楚萧\xa0\xa0', '李光洁\xa0\xa0'] 
熊出没·原始时代 	 7.9 	 http://imgwx4.2345.com/dypcimg/img/9/67/s203231.jpg 	 ['熊大\xa0\xa0', '熊二\xa0\xa0'] 
反贪风暴4 	 9.8 	 http://imgwx5.2345.com/dypcimg/img/a/67/s202697.jpg?1553159231 	 ['古天乐\xa0\xa0', '郑嘉颖\xa0\xa0'] 
掠食城市 	 9.1 	 http://imgwx3.2345.com/dypcimg/img/8/67/s201719.jpg?1546929260 	 ['海拉·西尔玛\xa0\xa0', '雨果·维文\xa0\xa0'] 
```

![文件截图](./imgs/2.jpg)

##### 项目代码

[getmovie.py传送门](https://github.com/codeccc/python-segments/blob/master/file/get_movie.py)