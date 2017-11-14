import conversionDialogBox as fileOpener



def findFileType():
	pass


def inputFile():
	# Get [fileObj, path, fileName, extension]:
	return fileOpener.run() 

def outputFile(obj, toFormat=False):
	fileObj = obj[0]
	path = obj[1]
	fileName = obj[2]
	extension = obj[3]

	print fileName, toFormat





if __name__ == "__main__":
	inputFile = inputFile()
	outputFile = outputFile(inputFile)