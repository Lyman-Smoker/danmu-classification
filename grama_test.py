#!/usr/bin/python3

import re

print(re.search('www.runoob.coms', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配