"""
File Sorter
Made by Liam McBride
mailmcbride56@gmail.com
"""

from os import listdir
import os.path
import shutil

#Put path between the quotes if you want this to run a certain directory without you typing it in everytime
filePath = ""

#Find files in folder
def FindFiles(fPath):
    fs = []
    
    for f in listdir(fPath):
        fs.append(f)
    return fs
#Uses FindFiles to populate and return a list of the file names
def FindNames(fPath):
    n = []
    for f in FindFiles(fPath):
        n.append(os.path.splitext(f)[0])
        
    return n
#Uses FindFiles to populate and return a list of the file extensions
def FindExts(fPath):
    n = []
    for f in FindFiles(fPath):
        n.append(os.path.splitext(f)[1])
    return n
    
#Creates folder name in proper format
def FolderName(fExt):
    return (filePath + '/' + (fExt[1:]).upper() + '_files')

#Creates new folder based off of ext using FolderName()
def CreateNewFolder(fExt):
    os.mkdir(FolderName(fExt))
    
#Moves file to folder
def MoveFile(fName, fExt, fDest):
    shutil.move(filePath + '/' + fName + fExt, fDest)

#Searches for pre-existing ext folder to make sure two folders are not created
def SearchForFolder(fName, fExt):
    done = False
    #this for loop searches each name in the FindNames() list, for each one it checks if the folder already exists
    for name in FindNames(filePath):
        folName = FolderName(fExt)
        if(filePath + '/' + name == folName):
            MoveFile(fName, fExt, FolderName(fExt))
            done = True
    #If the folder doesn't exist it creates a new one with correct naming convention
    if(done == False):
        CreateNewFolder(fExt)
        MoveFile(fName, fExt, FolderName(fExt))

#Main process Loop, this repeats endlessly until the program is shut down.
while(filePath == ''):
    filePath = input('Please enter a file path in the format dir/dir/dir/Desktop\n')
try:
    while True:
        i = 0
        for f in FindNames(filePath):
            if(i == len(FindNames(filePath))):
                break 
            if(FindExts(filePath)[i] != '' and FindFiles(filePath)[i] != 'FileSorter.py'):
                SearchForFolder(FindNames(filePath)[i], FindExts(filePath)[i])
            i += 1
except:
    print('Your Directory was incorrectly formatted or did not exits. Please re-launch and try again.')
    input('Press Enter to close')