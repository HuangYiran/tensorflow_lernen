#_*_coding:utf-8_*_
import re

tabu_words = {"字幕","说话人","雅黑","翻译：","校对：","飞天","小小","歌,NTP", "根据真实事件改编","片名："}

data = ""
f = open('../result/conversation_2', 'r')
for line in f:
    print(line)
    ob = False 
    for word in tabu_words:
        if re.search(word, line):
            print("------delete")
            ob = True
    if not ob:
        data = data + "$" + line
f.close()

data, _ = re.subn("-", "$\n", data)
data = data.split("$")
with open('../result/conversation_2', 'w') as f:
    for d in data:
        f.write(d)
