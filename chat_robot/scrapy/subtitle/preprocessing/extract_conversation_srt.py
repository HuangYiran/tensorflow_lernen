import os
import chardet

name_list = []
for root, dirs, files in os.walk("../result/srt"):
    for f in files:
        name_list.append(os.path.join(root, f))

DESTINATION_FILE = "../result/conversation"
destination_file = open(DESTINATION_FILE, 'a')

for name in name_list:
    print("file: " + name)

    with open(name) as f:
        for line in f:
            try:
                is_chinese = False
                li  = line.decode(chardet.detect(line)['encoding'])
                for ch in li:
                    if u'\u4e00' <= ch <= u'\u9fff':
                        is_chinese = True
                if is_chinese:
                    destination_file.write(line)
                else:
                    continue
            except:
                print("--------ununicode error:")
destination_file.close()
