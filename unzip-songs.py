import os
import zipfile

for root, dirs, files in os.walk("fumen"):
    for name in files:
        if os.path.splitext(name)[-1]=='.zip':

            print(os.path.join(root, name))
            zfile = zipfile.ZipFile(os.path.join(root, name))
            tja_count = 0
            multi_tja_suffix = ""
            for f in zfile.infolist():

                ext = f.filename.split('.')[-1]
                if ext == "tja":
                    tja_count+=1
                if tja_count>1:
                    multi_tja_suffix=str(tja_count)
                if ext == "ogg":
                    multi_tja_suffix = ""
                data = zfile.read(f)
                with open(root + '/main'  + multi_tja_suffix+'.' + ext, 'wb') as fw:
                    fw.write(data)
            os.remove(os.path.join(root, name))
