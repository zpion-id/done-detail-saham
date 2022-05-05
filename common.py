import csv
import os

def path_join(path_list:list):
    return os.path.join(*path_list)

def file_exist(file_path):
    if os.path.isfile(file_path):
        return True
    return False

def size_file(file_path):
    return os.path.getsize(file_path)

def file_name(tick:str,y:str, m:str, d:str):
    return tick+'-'+y+m+d+' - Sheet1.csv'

def create_csv(path_csv:str):
    with open(path_csv,'w', encoding='UTF8') as f :
        write = csv.writer(f)
        write.writerow('Time,Stock,Brd,Price,Qty,BT,BC,SC,ST'.split(','))