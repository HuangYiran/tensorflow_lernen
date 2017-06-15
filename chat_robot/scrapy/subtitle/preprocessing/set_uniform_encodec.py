import os
import chardet

for root, dirs, files in os.walk("../result/"):
    for f in files:
        relative_name = os.path.join(root, f)
        print(relative_name)
        with open(relative_name, 'r') as fi:
            data = fi.read()
        encoding = chardet.detect(data)['encoding']
        print(encoding)
        try:
            content = data.decode(encoding)
            if encoding  not in {'utf-8'}:
                print("encoding...")
                content.encode('utf-8')
            with open(relative_name, "w" ) as fi:
                print("writing ... ")
                fi.write(content.encode('utf-8'))
        except:
            print("except: unknown")
            os.rename(relative_name, root + "/" + "unchange/" + str(f))
            continue
