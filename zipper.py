#!/usr/bin/python3

import shutil
import sys
import os
from zipfile import PyZipFile

formats = list(i[0] for i in shutil.get_archive_formats())
form = list(i[0] for i in formats)
# TODO more than zip


def unzip():
    for compressed in sys.argv[2:]:
        if FileNotFoundError:
            print('No file or folder named: ' + compressed)
        else:
            PyZipFile(compressed).extractall()


def compress():
    if sys.argv[2] not in form:
        print('Bros small small')
    else:
        archive = formats[form.index(sys.argv[2])]
        for name in sys.argv[3:]:
            if name.endswith('/'):
                name = name[:-1]
                root = name[:name.rfind('/')] + '/'
            else:
                root = name[:name.rfind('/')] + '/'
            if os.path.exists(name):
                shutil.make_archive(os.path.basename(name), str(archive), root, os.path.basename(name))
            else:
                print('No File or Folder named: ' + os.path.basename(name))
 

try:
    if len(sys.argv) <= 3:
        print('Zipper by Jay version 1.0')
        print('/usr/bin/zipper')
        print('Usage: zipper [zip|unzip] ' + str(form[0:]).replace('\'', '').replace(', ', '|') + ' [file|folder]')
        for i in range(len(form)):
            print('    ' + form[i] + '  -  ' + formats[i])
    else:
        if sys.argv[1] == 'zip':
            compress()
        elif sys.argv[1] == 'unzip':
            unzip()
except Exception as e:
    print(e)
    
    

