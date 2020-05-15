# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:50:07 2020

@author: wang3241
"""
import os

directory = "new_pytorch_project"
root_path = './'+ directory

try:
    os.mkdir(root_path)
    print("Template '%s' created" % directory)
except FileExistsError:
    print("Template '%s' already exists" %directory)

main_dir = ['data_loader', 'model', 'saved', 'utils']
for i in range(len(main_dir)):
    dir_path = str(root_path) + '/' + str(main_dir[i])
    try:
        # create sub-directory
        os.mkdir(dir_path)
        print("Directory '%s' created" % (main_dir[i]))
    except FileExistsError:
        print("Directory '%s' already exists " % (main_dir[i]))
        
# create files in utils folder
filename1 = '__init__.py'
filename2 = 'util.py'
file_path = str(root_path) + '/utils/'
if not os.path.exists(file_path+filename1):
    with open(file_path + filename1, 'w') as f:
        f.write('from .util import *')
    f.close
    print("file '%s' created" % filename1)
else:
    print(" '%s' already exists" % filename1)
if not os.path.exists(file_path+filename2):
    with open(file_path + filename2, 'w') as f:pass
    f.close()
    print("file '%s' created" % filename2)
else:
    print(" '%s' already exists" % filename2)

# create files in data_loader folder
filename3 = 'data_loader.py'
file_path = str(root_path) + '/data_loader/'
if not os.path.exists(file_path+filename1):
    with open(file_path + filename3, 'w') as f:pass
    f.close()
    print("file '%s' created" % filename3)
else:
    print(" '%s' already exists" % filename3)

# create empty train.py and test.py file
file_list = ['config.json' , 'train.py', 'test.py']
file_path = root_path+ '/'
for i in range(len(file_list)):
    if not os.path.exists(file_path + file_list[i]):
        with open(file_path + file_list[i], 'w') as f:pass
        f.close()
        print("file '%s' created" % (file_list[i]))
    else:
        print(" '%s' already exists" % (file_list[i]))
    

