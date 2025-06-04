#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor  : Laudemir Oliveira
# @E-mail : laudemir.oliveira@gmail.com
# @Date   : 17-03-2024 - domingo
# @Version: 2024-78
#
import os
import argparse
import locale
import time
from sys import argv


# Definir a localizaçao para o portugues
#locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

t_struct   = time.localtime()
t_formated = time.strftime('%d-%m-%Y - %a - %H:%M')
y_formated = time.strftime('%Y')
dy_formated = int(time.strftime('%j'))
##
# Variaveis
_permission = 0o775 #rwxrwxr-x

data1 = f"""#!/usr/bin/env python3
# coding: utf-8
#
# @Autor....: 
# @E-mail...: 
# @Date.....: {t_formated}
# @Version..: {y_formated}-{dy_formated}
#
#

"""
file_name = os.path.basename(argv[0])

data2 = """def main():
    print("Hello World!")
    
    
if __name__ == "__main__":
    main()

"""

parser = argparse.ArgumentParser()

parser.add_argument("file", help="create a python template file of given name")
parser.add_argument("-m", "--main", action="store_true", help="add tags [if __name__ == \"__main__\"] to file")
parser.add_argument("-o", "--overwrite", action="store_true", help="overwrite the file if it exists")
args = parser.parse_args()

##
# Functions
def file_exists(_file):
    return os.path.exists(_file)

def file_create(_file, main_flag):
    if main_flag:
        with open(_file, "w") as f:
            f.write(data1 + data2)
    else:
        with open(_file, "w") as f:
            f.write(data1)
    f.close()
    os.chmod(_file, _permission)


##
# ajuda
_help=f"""[{args.file}] already exists!
usage: {file_name} -o {args.file} to overwrite or change the file name"""


##
# begins
file_flag = False
main_flag = False
overwrite_flag = False

if (args.main):
    main_flag = True

if (args.overwrite):
    overwrite_flag = True

if (args.file):
    file_flag = True


if file_flag:
    if overwrite_flag:
        file_create(args.file, main_flag)
    elif not file_exists(args.file):
        file_create(args.file, main_flag)
    else:
        print(_help)
else:
    print(_help)

