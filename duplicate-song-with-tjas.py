import os
import zipfile
import shutil

FILE_LOCATIONS = ['fumen/JPOP/', 'fumen/Anime/', 'fumen/Classic/', 'fumen/Game/', 'fumen/Kid/', 'fumen/Namco/', 'fumen/Varity/', 'fumen/Vocaloid/', 'fumen/Others/']
str_dup_tja=""
for category_dir in FILE_LOCATIONS:
    songs_dir = os.listdir(category_dir)
    for song_dir in songs_dir:
        if os.path.isdir(os.path.join(category_dir,song_dir)):
            files = os.listdir(os.path.join(category_dir,song_dir))
            if len(files)<3:continue
            elif len(files)==3:
                print(os.path.join(category_dir,song_dir))
                if not os.path.exists(os.path.join(category_dir,song_dir+"-dup")):
                    os.makedirs(os.path.join(category_dir,song_dir+"-dup"))
                shutil.copyfile(os.path.join(category_dir,song_dir,"main.ogg"), os.path.join(category_dir,song_dir+"-dup","main.ogg"))
                shutil.move(os.path.join(category_dir,song_dir,"main2.tja"), os.path.join(category_dir,song_dir+"-dup","main.tja"))

            else:
                str_dup_tja+=os.path.join(category_dir,song_dir)+"\n"
print("songs with more than two tjas:")
print(str_dup_tja)
print("please manually deal with above")
