#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13 19:59:16
# @Author  : Zoey Huang (1768771373@qq.com)
# @Link    : 计算字符串中the出现的次数——正则表达式
# @Version : 1.0

import re

string = "The quick brown for jumps over the lazy dog."
string_list = string.split()

pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output  #38: {0:d}".format(count))
