'''
Author: your name
Date: 2020-10-28 14:58:36
LastEditTime: 2021-01-23 14:51:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: Practice file.py
'''
import re
import numpy as np
filename = 'data.txt'
writedata = 'data2.txt'


def FindFrameHead(filename1, filename2):
    with open(filename1) as file:
        contents = file.readlines()
    f = open(filename2, 'w')
    framehead = re.compile(r'AA 55')
    for line in contents:
        f.writelines(framehead.sub(r'\n\nAA 55', line))
    f.close()


def FindFrameHead2(filename1, filename2):
    with open(filename1) as file:
        contents = file.readlines()
    f = open(filename2, 'w')
    framehead = re.compile(r'' + headstring + '')
    for line in contents:
        f.writelines(framehead.sub(r'\n\n' + headstring + '', line))
    f.close()


headstring = input("请输入数据分离标识:")
FindFrameHead2(filename, writedata)
print('数据分离完成！')
