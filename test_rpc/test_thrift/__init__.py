#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'

import os

'''
Usage: thrift [options] file
Options:
    -version    查看版本号
    -o dir      gen-*包 的生成位置(默认当前目录)
    -out dir    代码文件生成位置,会在指定位置生成namespace包(默认：创建gen-*文件夹，在该文件夹中生成namespace包)
    --gen STR   指定语言生成代码，
                格式：language[:key1=val1[,key2[,key3=val3]]]

    --help      其他请使用帮助参数
'''


if __name__ == '__main__':
    os.system('thrift -out . -gen py hello_world.thrift')