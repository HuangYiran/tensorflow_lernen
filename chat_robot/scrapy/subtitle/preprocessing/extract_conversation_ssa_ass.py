import os
import chardet

name_list = []
for root, dirs, files in os.walk("../result/ssa/"):
    for f in files:
        name_list.append(os.path.join(root, f))
for root, dirs, files in os.walk("../result/ass/"):
    for f in files:
        name_list.append(os.path.join(root, f))

DESTINATION_FILE = "../result/conversation_2"
destination_file = open(DESTINATION_FILE, 'a')

for name in name_list:
    print("file:" + name)

    with open(name) as f:
        for line in f:
            try:
                li = line.decode(chardet.detect(line)['encoding'])
                index_von = 0
                index_to = len(li)
                for i , ch in enumerate(li):
                    if u'\u4e00' <= ch <= u'\u9fff':
                        index_von = i
                        break;
                ob = u'\u4e00' <= li[index_to -1 ] <= u'\u9fff'
                ob = not ob
                while ob:
                    index_to = index_to -1
                    ob = u'\u4e00' <= li[index_to -1] <= u'\u9fff'
                    ob = not ob
                    if index_to == 0:
                        break
                if index_von <= index_to:
                    li = li[index_von: index_to]
                else:
                    print("error:..........")
                li = li.encode('utf-8')
                li = li.split('}')[-1]
                li = li.split('\N')[0]
                if len(li) != 0 and index_von != 0:
                    destination_file.write(li)
                    destination_file.write('\n')
            except:
                print("----------ununicode error:")
destination_file.close()
