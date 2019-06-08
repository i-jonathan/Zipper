#!/usr/bin/python3

import shutil
import sys
from zipfile import PyZipFile


# TODO filenotfound, more than zip
def unzip():
    for compressed in sys.argv[2:]:
        if FileNotFoundError:
            print('No file or folder named: ' + compressed)
        else:
            PyZipFile(compressed).extractall()


def zip():
    for name in sys.argv[2:]:
        if FileNotFoundError:
            print('No file or folder named: ' + name)
        else:
            shutil.make_archive(name, 'zip', root_dir=None, base_dir=name)


try:
    # if len(sys.argv) <= 2:
    #     print('Zipper by Jay version 1.0')
    #     print('/usr/bin/zipper')
    #     print('Usage: zipper [zip|unzip] [file|folder]')
    # else:
    if sys.argv[1] == 'zip':
        zip()
    elif sys.argv[1] == 'unzip':
        unzip()
except Exception:


