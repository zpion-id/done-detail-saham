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
    with open(path_csv,'x', encoding='UTF8') as f :
        write = csv.writer(f)
        write.writerow('blank'.split(','))

def read_csv(path_csv:str):
    line = []
    with open(path_csv,'r') as f :
        for l in f.readlines():
            if l.find('\t\n') == -1 :
                print('data sudah diformat')
                saved = False
                break
            if l.find('\t\n') >= 0 :
                l = l.replace('\t\n','\n')
                l = l.replace(',','')
                l = l.replace('\t',',')
                line.append(l)
                saved =True
                #print(l)
    return line, saved

def write_new_format(path_csv:str, lines):
    with open(path_csv, 'w') as f :
            f.writelines(lines)