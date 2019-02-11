# module 4 exercise: system modules
import os.path
import os
import glob
import shutil
import tkinter as tk
import tkinter.filedialog
import sys


# function to create a new file, borrowing from Linux
def touch(filename) :
    fh = open(filename, 'a')
    fh.close()
    
# function to write to file
def writeFile(filename, str) :
    fh = open(filename, 'a')
    fh.write(str)
    fh.close()    
    
# create a directory called python_test if it's not already there
if not os.path.isdir('python_test') :   # no directory path: look for python_test in current directory
    os.mkdir('python_test')
    
# go this directory
os.chdir('python_test')

# create the following directory hierarchy:
# python_test
#  |
#  |--dirA
#  |   |--file1.txt
#  |   |--dirB
#  |       |--file33.txt
#  |
#  |--dirC
#  |   |--file3.txt
#  |
#  |--file4.py
'''

# create the directory tree above
os.mkdir('dirA')
os.mkdir('dirC')
os.mkdir(os.path.join('dirA', 'dirB'))

writeFile(os.path.join('dirA', 'file1.txt'), '1111111\n')
writeFile(os.path.join('dirC', 'file3.txt'), '33333\n')
writeFile(os.path.join('dirA', 'dirB', 'file33.txt'), '33_33_33\n')

touch('file4.py')
'''
'''

# change the name of file33 under dirB to file33_33
Path = os.path.join('dirA', 'dirB')
os.rename(os.path.join(Path, 'file33.txt'), os.path.join(Path, 'file33_33.txt'))
                  # source                        # destination


# list file, show file size
print(os.path.getsize('file4.py'))        # show size of file4, which is in currrent directory 
print(os.listdir('.'))                    # list files in current directory
print(glob.glob('d*'))                    # list filenames starting with d in current directory
print(glob.glob(os.path.join('dirA','f*')))      # list filenames starting with f in dirA

'''
# python_test
#  |
#  |--dirA
#  |   |--file1.txt
#  |   |--dirB
#  |       |--file33.txt
#  |
#  |--dirC
#  |   |--file3.txt
#  |
#  |--file4.py

'''

# os walk: recursively print and get list of files / directories
# set p to current directory
p = os.getcwd()
for (path, dirlist, filelist) in os.walk(p) :
    for d in dirlist :
        print(os.path.join(path, d))
    for f in filelist :
        print(os.path.join(path,f))

'''
'''
# copy and move files and directories with list of files / directories
# a. move file4.py into dirA
shutil.move('file4.py', 'dirA')

# b. make a copy of dirC and call it copydir in the same parent directory
shutil.copytree('dirC', 'copydir')
'''

# python_test
#  |
#  |--dirA
#  |   |--file1.txt
#  |   |--file4.py
#  |   |--dirB
#  |       |--file33.txt
#  |
#  |--dirC
#  |   |--file3.txt
#  |
#  |--copydir
#      |-- file3.txt

'''
# Directory selection with GUI
path = os.getcwd()                       # path is current dir 
mw = tk.Tk()                             # create a main window
p = tk.filedialog.askdirectory(initialdir=path)     # create dile dialog window
print("Working directory:", p)           # 


'''
# command line argument
if len(sys.argv) == 0 :
    print("no command line argument")
else :
    for n,arg in enumerate(sys.argv) :
        print(n,":",arg)
