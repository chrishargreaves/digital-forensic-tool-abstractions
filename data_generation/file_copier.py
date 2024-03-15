import os
import shutil
import sys
import time
import datetime

print('starting')
print(datetime.datetime.utcnow())
target_root = sys.argv[1]
print(target_root)
input("Press enter to continue: ")

print('creating two folders')
print(datetime.datetime.utcnow())
os.mkdir(os.path.join(target_root, 'del_demo'))
os.mkdir(os.path.join(target_root, 'del_demo', 'folder1'))
os.mkdir(os.path.join(target_root, 'del_demo', 'folder2'))

input('Press enter to continue: ')

print('copying missed me example...')
print(datetime.datetime.utcnow())
missed_in_file = os.path.join('test_files', 'missedme.txt')
shutil.copyfile(missed_in_file, os.path.join(target_root, 'missedme.txt'))

input('Press enter to continue: ')


print('generating deleted file example...')
print(datetime.datetime.utcnow())
todo_path_in = os.path.join('test_files', 'del_demo', 'folder1', 'FIRST.TXT')
todo_path_out = os.path.join(target_root, 'del_demo', 'folder1', 'FIRST.TXT')
print('copying file 1...')
shutil.copyfile(todo_path_in, todo_path_out)

input('Press enter to continue: ')

print('deleting file 1...')
print(datetime.datetime.utcnow())
os.remove(todo_path_out)

input('Press enter to continue: ')

dontdo_path_in = os.path.join('test_files', 'del_demo', 'folder2', 'SECOND.TXT')
dontdo_path_out = os.path.join(target_root, 'del_demo', 'folder2', 'SECOND.TXT')
print('copying file 2...')
print(datetime.datetime.utcnow())
shutil.copyfile(dontdo_path_in, dontdo_path_out)

#input('Press enter to continue: ')

#print('deleting file 2...')
#os.remove(dontdo_path_out)

print('done')
print(datetime.datetime.utcnow())