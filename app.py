import streamlit as st

import os
from common import (
    path_join,
    file_exist,
    read_csv,
    file_name,
    create_csv,
    write_new_format,
    size_file
)
from datetime import datetime

'''
## DONE DETAIL SAHAM
'''
st.write(os.getcwd())

tick = st.text_input("KODE SAHAM", value="ICBP INDF JSMR MYOR PTBA TLKM UNVR", help="Kode saham dipisahkan dengan spasi", placeholder='ICBP INDF JSMR MYOR PTBA TLKM UNVR').split(' ')
y = st.text_input('TAHUN', value=datetime.now().year, max_chars=4, help='Tahun', placeholder='2022')
m = st.text_input('BULAN', value=datetime.now().strftime('%m'), max_chars=2, help='Bulan', placeholder='01')
dates = st.text_input('TANGGAL',max_chars=60,help='Tanggal dipisahkan dengan spasi', placeholder="01 02 03").split(' ')

root = os.getcwd()
done_dir = os.path.join(root,'done_detail')
file_path = ''

def create_new_csv():
    count_file = 0
    for t in tick :
        for d in dates:
            file_path = path_join([done_dir, t, y, file_name(t, y, m, d)])
            if file_exist(file_path):
                st.warning('File sudah ada : '+ file_path)
            if not file_exist(file_path):
                count_file += 1
                st.success('Create file ke - '+ str(count_file) +': '+ file_path)
                create_csv(file_path)

def reformat_csv():
    for t in tick :
        for d in dates:
            file_path = path_join([done_dir, t, y, file_name(t, y, m, d)])
            if file_exist(file_path):
                lines, saved = read_csv(file_path)    
                if saved :
                    write_new_format(file_path, lines)
                    st.success('reformat : '+ file_path)
            if not file_exist(file_path):
                st.warning('file tidak ada : '+ file_path)


list_files = []
for t in tick :
    for d in dates:
        file_path = path_join([done_dir, t, y, file_name(t, y, m, d)])
        if file_exist(file_path):
            list_files.append(file_path + ' size : ' + str(size_file(file_path)) + ' byte')
            


if dates[0] == "":
    st.warning('masukan tanggal')
else :
    if st.button('create csv'):
        create_new_csv()
        st.success("create csv selesai")
if len(list_files)>0 :
    for i in list_files :
        st.write(i)
    if st.button('reformat csv'):
        reformat_csv()
        st.success("Reformat "+ str(len(list_files)) +"file selesai")


# Cek apakah sudah complete di tambahkan datanya.