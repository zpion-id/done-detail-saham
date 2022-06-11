import os
from common import (
    path_join,
    file_exist,
    size_file,
    file_name,
    create_csv
)

tick = 'ICBP INDF JSMR MYOR PTBA TLKM UNVR'.split(' ')
year = '2022'
month = '06'
date = '02 03 06 07 08 09 10'.split(' ')

if __name__ == "__main__":
    root = os.getcwd()
    done_dir = os.path.join(root,'done_detail')
    
    file_path = ''
    print(file_path)
    
    for t in tick :
        for d in date:
            file_path = path_join([done_dir, t, year, file_name(t, year, month, d)])
            if file_exist(file_path):
                print('File sudah ada : '+ file_path)
            if not file_exist(file_path):
                print('Create file : '+ file_path)
                create_csv(file_path)
            