from bs4 import BeautifulSoup as bs
from io import BytesIO, TextIOWrapper
import requests
import zipfile
import os
import codecs
import sys
import shutil


FILE_LOCATIONS = ['fumen/JPOP/', 'fumen/Anime/', 'fumen/Classic/', 'fumen/Game/', 'fumen/Kid/', 'fumen/Namco/', 'fumen/Varity/', 'fumen/Vocaloid/', 'fumen/Others/']
TMP_DIR = 'tmp/'
PROGRESS_FILE = 'bulk-download-progress.csv'
NOT_DOWNLOADED = 'not_downloaded.csv'
ERROR_FILE = 'errors.txt'
SKIP = -1
JPOP = 0
Anime = 1
Classic = 2
Game = 3
Kid = 4
Namco = 5
Varity = 6
Vocaloid = 7
Others = 8

def __main__():
    completed = []
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            completed.append(f.read().split('\n'))

    filejString = []
    if os.path.exists('list/JPOP.txt'):
        with open('list/JPOP.txt', 'r', encoding = 'utf8') as j:
            filejString.append(j.read().split('\n'))
    filejString = filejString[0]

    fileaString = []
    if os.path.exists('list/Anime.txt'):
        with open('list/Anime.txt', 'r', encoding = 'utf8') as a:
            fileaString.append(a.read().split('\n'))
    fileaString = fileaString[0]

    filecString = []
    if os.path.exists('list/Classic.txt'):
        with open('list/Classic.txt', 'r', encoding = 'utf8') as c:
            filecString.append(c.read().split('\n'))
    filecString = filecString[0]

    filegString = []
    if os.path.exists('list/Game.txt'):
        with open('list/Game.txt', 'r', encoding = 'utf8') as g:
            filegString.append(g.read().split('\n'))
    filegString = filegString[0]

    filekString = []
    if os.path.exists('list/Nursey.txt'):
        with open('list/Nursey.txt', 'r', encoding = 'utf8') as k:
            filekString.append(k.read().split('\n'))
    filekString = filekString[0]

    filenString = []
    if os.path.exists('list/Namco.txt'):
        with open('list/Namco.txt', 'r', encoding = 'utf8') as n:
            filenString.append(n.read().split('\n'))
    filenString = filenString[0]

    filevString = []
    if os.path.exists('list/Variety.txt'):
        with open('list/Variety.txt', 'r', encoding = 'utf8') as v:
            filevString.append(v.read().split('\n'))
    filevString = filevString[0]

    filedString = []
    if os.path.exists('list/Vocaloid.txt'):
        with open('list/Vocaloid.txt', 'r', encoding = 'utf8') as d:
            filedString.append(d.read().split('\n'))
    filedString = filedString[0]
    
    setup()

    progress = open(PROGRESS_FILE, 'w', encoding = 'utf8')
    not_downloaded = open(NOT_DOWNLOADED, 'w', encoding = 'utf8')
    errors = open(ERROR_FILE, 'w', encoding = 'utf8')

    files = os.listdir('fumen\\')
    for file in files:  # 遍历文件夹
        if not os.path.isdir(os.path.join('fumen\\',file)):  # 判断是否是文件夹，不是文件夹才打开
            title,ext = os.path.splitext(file)[0],os.path.splitext(file)[-1]
            #if '-2' in title:
            #    continue
            if not ext=='.zip':
                continue
            print(file)

            status = process(title , filejString , fileaString , filecString , filegString , filekString , filenString , filevString , filedString)

            if status != SKIP:
                dirname = FILE_LOCATIONS[status] + title
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                shutil.move('fumen\\'+file, dirname)



                    # filename = 'fumen/'  + title +  '.zip'
                    # if os.path.exists(filename):
                    #     filename = 'fumen/' + title + '-2.zip'
                    # print("writing file:",filename)
                    # with open(filename, 'wb') as fw:
                    #     fw.write(dl.content)

                    #status = process(title , filejString , fileaString , filecString , filegString , filekString , filenString , filevString , filedString)

                    # if status != SKIP:
                    #     dirname = FILE_LOCATIONS[status] + title
                    #     if not os.path.exists(dirname):
                    #         os.makedirs(dirname)
                    #     for f in os.listdir(TMP_DIR):
                    #         shutil.move(TMP_DIR + f, dirname)
                    # else:
                    #     for f in os.listdir(TMP_DIR):
                    #         os.remove(TMP_DIR + f)
                    #     not_downloaded.write(line)
                    #     print('=== SKIPPED ===')


def setup():
    for f in FILE_LOCATIONS:
        if not os.path.exists(f):
            os.makedirs(f)
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

def process(title , filejString , fileaString , filecString , filegString , filekString , filenString , filevString , filedString):
    title = title[:-2]
    if title in filejString:
        return JPOP
    if title in fileaString:
        return Anime
    if title in filecString:
        return Classic
    if title in filegString:
        return Game
    if title in filekString:
        return Kid
    if title in filenString:
        return Namco
    if title in filevString:
        return Varity
    if title in filedString:
        return Vocaloid
    return Others

if __name__ == '__main__':
    __main__()
