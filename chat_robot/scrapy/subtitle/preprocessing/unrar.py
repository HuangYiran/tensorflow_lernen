# this program dosen't work. wenn i try to unrar a file,
# i get the info "no file to extract" back
# i can't explain why
# therefore i use Keka to extrakt the file
import rarfile
import os

name_list = []
for root, dirs, files in os.walk("../result/rar/"):
    for f in files:
        name_list.append(f)
    break

for name in name_list:
    relative_filename = "../result/rar/" + str(name)
    rar = rarfile.RarFile(relative_filename)
    rar.extractall()
    rar.close()
