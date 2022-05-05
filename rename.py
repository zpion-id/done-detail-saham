import os

root = 'done_detail'

#print(os.listdir(root))

path_file =[]
new_file = []
for dir in os.listdir(root):
    if os.path.dirname(os.path.join(root,dir)):
        for file in os.listdir(os.path.join(root,dir)):
            if os.path.isfile(os.path.join(root,dir,file)):
                path_file.append(os.path.join(root,dir,file))

for file in path_file:
    new = file.replace('Mar', '03')
    if os.path.isfile(new):
        print('file sudah ada : '+ file)
    else:
        os.rename(file, new)
        #print(new)
    #new_file.append(file.replace('Jan', '01'))

#print(path_file)
#print(new_file)