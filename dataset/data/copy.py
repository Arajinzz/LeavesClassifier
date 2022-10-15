import os
from shutil import copyfile

for filename in os.listdir('.'):
    if filename == '__pycache__' or filename == 'copy.py':
        continue
    for f in os.listdir(filename):
        copyfile(os.path.join(filename, f), '../../gui/image/'+filename+'.jpg')
        break