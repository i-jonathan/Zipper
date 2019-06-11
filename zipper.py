#!/usr/bin/python3

import shutil
import sys
import os

formats = list(i[0] for i in shutil.get_archive_formats())
form = list(i[0] for i in formats)


def unzip():
    for compressed in sys.argv[3:]:
        try:
            if os.path.exists(compressed):
                shutil.unpack_archive(compressed)
            else:
                print('No file or folder named: ' + compressed)
        except ValueError:
            print('We might get there one day. But for now, Unsupported archive format')


def compress():
    if sys.argv[2] not in form:
        print('Bros small small')
    else:
        archive = formats[form.index(sys.argv[2])]
        for name in sys.argv[3:]:
            if name.endswith('/'):
                name = name[:-1]
                splitter = os.path.split(name)
            else:
                splitter = os.path.split(name)
            root = splitter[0]
            if root == '':
                root = None
            if os.path.exists(name):
                shutil.make_archive(os.path.join(os.getcwd(), splitter[1]), str(archive), root, splitter[1])
            else:
                print('No File or Folder named: ' + os.path.basename(name))
 

try:
    if len(sys.argv) <= 3:
        print('Zipper by Jonathan Farinloye version 2.0')
        print(os.system('which zipper'))
        print('Usage: zipper [up|down] ' + str(form[0:]).replace('\'', '').replace(', ', '|') + ' [file|folder]')
        print('up     -  Compress a file or directory')
        print('down   -  Extract the contents of a compressed folder')
        for i in range(len(form)):
            print('    ' + form[i] + '  -  ' + formats[i])
    else:
        if sys.argv[1] == 'up':
            compress()
        elif sys.argv[1] == 'down':
            unzip()
except Exception as e:
    print(e)
    
    

