## Scrapy爬虫框架

### 简介

Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

其最初是为了 [页面抓取](http://en.wikipedia.org/wiki/Screen_scraping) (更确切来说, [网络抓取](http://en.wikipedia.org/wiki/Web_scraping) )所设计的， 也可以应用在获取API所返回的数据(例如 [Amazon Associates Web Services](http://aws.amazon.com/associates/) ) 或者通用的网络爬虫。



###项目创建

#### 1.创建scrapy项目

在命令行中使用如下命令创建scrapy项目

```python
scrapy startproject [你的项目名称,如 example]
```

#### 2.建立基础爬虫

```python
cd [你的项目名称]
scrapy genspider [爬虫脚本名称,如 example] [要爬取的网站名称,如 example.com]
```



以 `example`为文件名，`test`为项目名，爬取域名为‘test.com‘，项目生成的目录如下：

example
│  scrapy.cfg
│  
└─example
    │  items.py
    │  middlewares.py
    │  pipelines.py
    │  settings.py
    │  __init__.py
    │  
    ├─spiders
    │  │  test.py
    │  │  __init__.py
    │  │  
    │  └─__pycache__
    │          __init__.cpython-37.pyc
    │          
    └─__pycache__
            settings.cpython-37.pyc
            __init__.cpython-37.pyc



#### 文件说明

**scrapy.cfg**

项目中会自动生成`scrapy.cfg`文件，文件内容如下：

```
# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.io/en/latest/deploy.html

[settings]
default = example.settings

[deploy]
#url = http://localhost:6800/
project = todayMoive
```

除去以"#"为开头的注释行，整个文件只声明了两件事： 一是默认设置文件的位置为 example 下的 settings 文件， 二是定义项目的名称为 example



**.pyc文件**

结尾的是同名Python程序编译得到的字节码文件，如 `settings.pyc`是`settings.py`的字节码文件，可以用来加快程序的运行速度，可以忽视。

空的`__init__.py`文件用于将它的上级目录变成一个模块，也就是第二层example模块下，如果没有`__init__.py`文件，它就只是一个单纯的文件夹。将文件夹进行模块化，可供后续Python进行导入使用。

**setings.py**

`settings.py`是上层目录中`scrapy.cfg`定义的设置文件。`settings.py`的内容如下：

```python
# -*- coding: utf-8 -*-

# Scrapy settings for example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'example (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# ......
# 中间有省略
# ......

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

```

**items.py**

`items.py`文件的作用是定义爬虫最终需要哪些项, items.py的内容如下:

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

```

**pipelines.py**

`pipelines.py`文件的作用是扫尾. Scrapy爬虫爬去了网页的内容后,这些内容怎么处理就取决于`pipelines.py`如何设置了.`pipelines.py`文件内容如下:

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ExamplePipeline(object):
    def process_item(self, item, spider):
        return item

```

**middlewares.py**

`middlewares.py`是介入到Scrapy的spider处理机制的钩子框架，您可以添加代码来处理发送给 [Spiders](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/spiders.html#topics-spiders)的response及spider产生的item和request。`middlewares.py`文件内容如下:

```python
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ExampleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ExampleDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

```

