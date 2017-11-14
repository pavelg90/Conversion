import os.path
from Tkinter import *
from tkFileDialog import askopenfilename
from tkMessageBox import *

def getFileName():

	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	
	extension = os.path.splitext(filename)[1]
	path = os.path.splitext(filename)[0]
	fileName = os.path.basename(filename).replace(extension, '')
	
	return path, fileName, extension

def getDesiredFormat():
	messagebox.showinfo("Information","Informative message")    


def run():
	path, fileName, extension = getFileName()
	fileObj = open(path + extension, 'r')
	return fileObj, path, fileName, extension


if __name__ == "__main__":
	getDesiredFormat()
	pass	