#coding:utf-8
import os

name_list = []
for root, dirs, files in os.walk('../result/'):
    for f in files:
        name_list.append(os.path.join(root, f))

for name in name_list:
    print("file: " + name)

    is_chinese = False
    with open(name) as f:
        try:
            data = f.read()
            content = data.decode('utf-8')
            for ch in content:
                if u'\u4e00' <= ch <= u'\u9fff':
                    is_chinese = True
        except:
            print("decode fail")
    if not is_chinese:
        print("--------- is not chinese")
        os.remove(name)
