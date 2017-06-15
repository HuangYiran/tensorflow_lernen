import os

dir_list = []
for root, dirs, files in os.walk("../result"):
    for d in dirs:
        dir_list.append(d)

for d in dir_list:
    if d in ("doc","zip", "docx", "DS_Store", "nfo", "rar", "sub", "idx", "txt", "html", "mp4", "JPG"):
        for root, dirs, files in os.walk("../result/" + str(d), topdown = False):
            for f in files:
                os.remove(os.path.join(root, f))
            for d in dirs:
                os.rmdir(os.path.join(root, d))
        os.rmdir(os.path.join("../result", str(d)))
