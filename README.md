## python-segments

日常编写/收集一些通用的代码片段



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

