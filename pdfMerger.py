import PyPDF2
import sys
import os

def confirmation():
    conf = input('Continue? [y]Yes [n]No \n')
    if conf == 'y':
        for file in pdfs:               #os.listdir(os.curdir):
            if file.endswith('.pdf'):
                merger.append(file)
        name = input('Name of the new file: \n')
        merger.write(name + '.pdf')
    elif conf == 'n':
        print('Operation aborted')
    else:
        print('Please choose a valid option')
        confirmation()

def addPdfs():
    add = input('Do you want to add another file? [y]Yes [n]No \n')
    if add == 'y':
        file2 = input('File to merge: ')
        pdfs.append(file2)
        addPdfs()
    elif add == 'n':
        print('Files to merge: ')
        for file in pdfs:               #os.listdir(os.curdir):
            if file.endswith('.pdf'):
                print(file)
        confirmation()
    else:
        print('Please choose a valid option')
        addPdfs()
    
merger = PyPDF2.PdfMerger()
pdfs = []
file = input('File to merge: ')
pdfs.append(file)
addPdfs()