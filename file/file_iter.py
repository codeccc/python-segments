# encoding=utf-8

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
