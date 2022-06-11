import os
from common import (
    read_csv,
    path_join,
    file_exist,
    file_name,
    write_new_format,
)
from config import (
    code,
    year,
    month,
    date
)

tick = code.split(' ')
y = year
m = month
dates = date.split(' ')


if __name__ == "__main__":
    root = os.getcwd()
    done_dir = os.path.join(root,'done_detail')

    file_path = ''
    print(file_path)
    
    for t in tick :
        for d in dates:
            file_path = path_join([done_dir, t, y, file_name(t, y, m, d)])
            if file_exist(file_path):
                lines, saved = read_csv(file_path)    
                if saved :
                    write_new_format(file_path, lines)
                    print('reformat : '+ file_path)
            if not file_exist(file_path):
                print('file tidak ada : '+ file_path)
