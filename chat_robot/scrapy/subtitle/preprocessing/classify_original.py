import os

file_list = []
for root, dirs, files in os.walk("../result/"):
    for f in files:
        file_list.append(f)
    break;

for filename in file_list:
    affix = filename.split(".")[-1]
    if not os.path.exists("../result/" + str(affix)):
        os.mkdir("../result/" + str(affix))
    relative_filename = "../result/" + str(filename)
    new_relative_filename = "../result/" + str(affix) + "/" + str(filename)
    os.rename(relative_filename, new_relative_filename)
