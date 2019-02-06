import operator
import numpy as np

def splitStringComma(line,item):
	SplitLine = line.split(',')
	#print SplitLine
	datFile = SplitLine[item]
	#print datFile
	return datFile

def splitString(line,item):
	SplitLine = line.split()
	#print SplitLine
	datFile = SplitLine[item]
	#print datFile
	return datFile	

def partHeightMatrix(partMatrix):
	#unpack part matrix
	studMatrix = []
	
	partID = splitStringComma(partMatrix,0)
	Depth = int(splitStringComma(partMatrix,1))
	Height = int(splitStringComma(partMatrix,2))
	Width = int(splitStringComma(partMatrix,3))
	StudCount = int(splitStringComma(partMatrix,5))
	
	print partID, "Brick is ",Width, "x" ,Depth, " and ", Height, "High"
	#print
	for i in range (0,Width):
		for j in range(0,Depth):
			if StudCount == 0:
				#print "X ",
				studMatrix.append(Height) #99 is currently the maximium height the model would reach - which is 33 bricks (as each 1 is a 1/3 of brick)
			else:	
				#print Height, " ",
				studMatrix.append(Height)

	modelHeightArray = np.array(studMatrix).reshape(Depth,Width);

	return modelHeightArray	
	
	
	
def studView(partMatrix,DictionaryOfPartsAndStuds):
	#unpack part matrix
	studMatrix = []
	partID = splitStringComma(partMatrix,0)
	Depth = int(splitStringComma(partMatrix,1))
	Height = int(splitStringComma(partMatrix,2))
	Width = int(splitStringComma(partMatrix,3))
	StudCount = int(splitStringComma(partMatrix,5))

	print partID, "Brick is ",Width, "x" ,Depth
	for i in range (0,Width):
		for j in range(0,Depth):
			if StudCount == 0:
				studMatrix.append(0) #Zero out for studless
			else:	
				studMatrix.append(1)
	modelStudArray = np.array(studMatrix).reshape(Depth,Width);
	DictionaryOfPartsAndStuds[partID]=modelStudArray
	return DictionaryOfPartsAndStuds
	#return modelStudArray
	
def getXYZDimensions(ldrLine):
	x = splitString(ldrLine,2)
	y = splitString(ldrLine,3)
	z = splitString(ldrLine,4)
	xyz = [x,y,z]
	print xyz
	return xyz

def highestPart(FileName):
	ListOfPartsAndHeights = []
	with open(FileName) as f:
		lineNumber = 0
		lines = f.readlines()		
		for line in lines:
			#print line[0]
			if line[0] == "1":
				lineNumber = lineNumber + 1
				print lineNumber
				partHeight = int(splitString(line,3))
				partFile = splitString(line,14)
				ListOfPartsAndHeights.append([partFile,partHeight])
				
		print

		print ListOfPartsAndHeights
		print

		ListOfPartsAndHeights.sort(key=lambda tup: tup[1],reverse = True)
		
		print

		print ListOfPartsAndHeights
		print
		highestPart = ListOfPartsAndHeights[-1] # Get the last item in a list
		print "Highest part is...",highestPart		
		return ListOfPartsAndHeights

def addAtPos(mat1, mat2, xypos): # From https://stackoverflow.com/questions/9886303/adding-different-sized-shaped-displaced-numpy-matrices
    '''
    Add two matrices of different sizes in place, offset by xy coordinates
    Usage:
      - mat1: base matrix
      - mat2: add this matrix to mat1
      - xypos: tuple (x,y) containing coordinates
    
	block1 = np.zeros((5,4))
	block2 = np.ones((3,2))
	pos = (2,1)
	print(addAtPos(block1, block2, pos))
	
	'''
    x, y = xypos
    ysize, xsize = mat2.shape
    xmax, ymax = (x + xsize), (y + ysize)
    mat1[y:ymax, x:xmax] += mat2
    return mat1	

def ldr2mat(width,depth):
	#=(E3-(E3+1)/2)*-2
	matxMaty = []
	widthInStuds = float(width/20)
	depthInStuds = float(depth/20)
	matx = int(float((depthInStuds-(depthInStuds+1)/2)*-2))
	maty = (int(widthInStuds-1)*-1)
	#print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	#print "Original Values",width,depth
	#print "Values in Studs",widthInStuds,depthInStuds
	#print "Values for Matrix: ", matx,",",maty
	#print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	matxMaty.append(matx)
	matxMaty.append(maty)
	#print matxMaty
	return matxMaty	
	
#================== MAIN CODE ==================

if __name__ == "__main__":
	print "...being run directly"

	part01 = "1 10 0 0 0 1 0 0 0 1 0 0 0 1 3031.dat"
	part02 = "1 4 0 -8 0 0 0 1 0 1 0 -1 0 0 3068b.dat"
	part03 = "1 4 20 -8 20 0 0 1 0 1 0 -1 0 0 3068b.dat"

	partMatrix01 = "'C:\\LDraw\\Parts\\3031.dat', 4, 1, 4, 1, 16"
	partMatrix02 = "'C:\\LDraw\\Parts\\s\\3068bs01.dat', 2, 1, 2, 0, 0"
	partMatrix03 = "'C:\\LDraw\\Parts\\3003.dat', 2, 3, 2, 1, 4"
	
	print "==================================="
	print "Part Height Matrix"
	partHeightMatrix01 = partHeightMatrix(partMatrix01)
	partHeightMatrix02 = partHeightMatrix(partMatrix03)
	
	print "==================================="
	
	pos = (1,0)
	print "Adding model arrays at...",pos
	print
	firstArray = partHeightMatrix02
	print firstArray
	secondArray = partHeightMatrix01
	print
	print secondArray
	print
	print(addAtPos(secondArray, firstArray, pos))
else:
	print("...being imported into another module")