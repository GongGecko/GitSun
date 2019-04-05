#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
打开 gtemp4.py 文本，
并删除每行开头的 delete_front_T1Var 个字符，
并每行开头添加 add_front_T1Var 字符串。
'''

__author__ = 'Gong Liuxu'


delete_front_T1Var = 6
add_front_T1Var = ''
input_file_T1Var = 'D:\EDisk\CodeTao\HTM\gtemp4.py'

def change_front_T2Fun(input_file_T1Var, add_front_T1Var, delete_front_T1Var):
    f = open(input_file_T1Var, 'r')
    lines = f.readlines()
    for line in lines:
        print(add_front_T1Var + line[delete_front_T1Var:-1])
    f.close()

if __name__ == '__main__':
    change_front_T2Fun(input_file_T1Var, add_front_T1Var, delete_front_T1Var)

