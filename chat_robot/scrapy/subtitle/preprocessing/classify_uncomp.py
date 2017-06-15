import os

name_list = []
relative_name_list = []
for root, dirs, files in os.walk("../result/"):
    for f in files:
        name_list.append(f)
        relative_name_list.append(os.path.join(root, f))

for name, relative_name in zip(name_list, relative_name_list):
    affix = name.split(".")[-1]
    if not os.path.exists("../result/" + str(affix)):
        os.mkdir("../result/" + str(affix))
    new_relative_name = "../result/" + str(affix) + "/" + str(name)
    os.rename(relative_name, new_relative_name)
