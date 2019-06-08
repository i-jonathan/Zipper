#!/usr/bin/python3

import shutil, sys
from zipfile import PyZipFile


def unzip():
    for compressed in sys.argv[2:]:
        PyZipFile(compressed).extractall()


def zip():
    for folder in sys.argv[2:]:
        shutil.make_archive(folder, 'zip', root_dir=None, base_dir=folder)


try:
    if sys.argv[1] == 'zip':
        zip()
    elif sys.argv[1] == 'unzip':
        unzip()
except Exception as e:
    print('Zipper by Jay version 1.0')
    print('/usr/bin/zipper')
    print(e)

