import os,datetime, time, sys
	
import brickDimensions
import studView
from random import randint
from copy import deepcopy
import numpy

print "No command line argument passed - using simple file name..."

def checkInput():
	userNumber = raw_input("Choose number 1-99? (q to quit) ")

	if userNumber == "q" or userNumber == "Q" or userNumber == "Quit":
		sys.exit()
	
	try:
		numberChosen = int(userNumber)		
		if numberChosen < 1 or numberChosen > 99:			
			print
			print "Opps that number is not between 1 and 99"
			userNumber = checkInput()	
		else:
			print "Good choice...",numberChosen	
			return numberChosen
	except:
		print
		print "Opps that's not a number"
		userNumber = checkInput()
		numberChosen = int(userNumber)
		return numberChosen

def timeStamp (): #Create timestamps
	ts = time.time()	
	dateTimeString = datetime.datetime.fromtimestamp(ts).strftime('%y%m%d%H%M')
	return (dateTimeString)	

def resetldrFile(fileName):	
	fileName = fileName
	LDrawFile = open(fileName, 'w').close()
	
def legoWriter(fileName,dateTimeStamp,ldrLine):
	null = 0
	print fileName
	if os.path.isfile(fileName): 
		LDrawFile = open(fileName, 'a')
		if "41539.dat" in ldrLine:
			LDrawFile.write('0 // Name: '+ fileName +'\n')
			LDrawFile.write('0 // Author:  BRICKALO ' + dateTimeStamp +'\n')
			LDrawFile.write('1 4 70 -8 70 0 0 1 0 1 0 -1 0 0 6141.dat'+'\n')
			LDrawFile.write('\n')
		elif "3031.dat" in ldrLine:
			LDrawFile.write('1 4 30 0 30 0 0 1 0 1 0 -1 0 0 6141.dat'+'\n')
		LDrawFile.write('\n')
	else:
		LDrawFile = open(fileName, 'w')
		LDrawFile.write('0 // Name: '+ fileName +'\n')
		LDrawFile.write('0 // Author:  BRICKALO ' + dateTimeStamp +'\n')
		LDrawFile.write('1 4 70 -8 70 0 0 1 0 1 0 -1 0 0 6141.dat'+'\n')
		LDrawFile.write('\n')
	print "WRITING LINE"
	LDrawFile.write(ldrLine)
	return fileName
	
def commentLine(comment):
	null = 0
	
def activeLineList(ldrLineList):
	#Example ldr line
	#1 69 -20 -24 -20 0 0 1 0 1 0 -1 0 0 3003.dat
	active = str(ldrLineList[0])
	colour = str(ldrLineList[1])
	width = str(ldrLineList[2])
	height = str(ldrLineList[3])
	depth = str(ldrLineList[4])
	m1 = str(ldrLineList[5])
	m2 = str(ldrLineList[6])
	m3 = str(ldrLineList[7])
	m4 = str(ldrLineList[8])
	m5 = str(ldrLineList[9])
	m6 = str(ldrLineList[10])
	m7 = str(ldrLineList[11])
	m8 = str(ldrLineList[12])
	m9 = str(ldrLineList[13])
	partID = str(ldrLineList[14])
	ldrLine = active + " " + colour + " " + width + " " + height+ " " + depth  + " " + m1 + " " + m2 + " " + m3 + " " + m4 + " " + m5 + " " + m6 + " " + m7 + " " + m8 + " " + m9 + " " + partID
	return ldrLine	
	
def activeLine(active,colour,width,height,depth,m1,m2,m3,m4,m5,m6,m7,m8,m9,partID):
	#Example ldr line
	#1 69 -20 -24 -20 0 0 1 0 1 0 -1 0 0 3003.dat
	active = str(active)
	colour = str(colour)	
	width = str(width)
	height = str(height)
	depth = str(depth)
	m1 = str(m1)
	m2 = str(m2)
	m3 = str(m3)
	m4 = str(m4)
	m5 = str(m5)
	m6 = str(m6)
	m7 = str(m7)
	m8 = str(m8)
	m9 = str(m9)
	ldrLine = active + " " + colour + " " + width + " " + height+ " " + depth  + " " + m1 + " " + m2 + " " + m3 + " " + m4 + " " + m5 + " " + m6 + " " + m7 + " " + m8 + " " + m9 + " " + partID
	return ldrLine
	
def upadteLastLine(line,item,height,maxValue):
	splitLine = line.split()
	print "===================================="
	print "OLD splitLine",splitLine	
	datFile = splitLine[item]
	splitLine[3] = (maxValue-1)*-8 #To keep the number negative if it already was.
	print "===================================="
	return splitLine	


def readAndModifyLastLineOfLDRFile(fileName,height,maxValue): #From https://stackoverflow.com/questions/327985/how-do-i-modify-the-last-line-of-a-file
	myFile = fileName
	# read the file into a list of lines
	lines = open(myFile, 'r').readlines()
	# now edit the last line of the list of lines
	oldLastLine = lines[-1]
	newLastLineList = upadteLastLine(oldLastLine,3,height,maxValue)
	newLastLine = " ".join(str(e) for e in newLastLineList)
	print "^^^^^^^^^^^^^^^^^^^","LDR LINE UPDATE","^^^^^^^^^^^^^^^^^^^"
	print "oldLastLine",oldLastLine
	print "newLastLine",newLastLine
	print "^^^^^^^^^^^^^^^^^^^"
	lines[-1] = newLastLine

	# now write the modified list back out to the file
	open(myFile, 'w').writelines(lines)	

def subMatrix( matrix, startRow, startCol, size): #FROM https://stackoverflow.com/questions/36692484/python-extracting-a-smaller-matrix-from-a-larger-one
	x = numpy.array(matrix)
	return x[startRow:startRow+size,startCol:startCol+size]

def checkBuildMatix(buildMatrix,listOfPartHeightMatrix,ldrLineAndPartsInfo,pos):
	print "= x = x = x = x = x = x = x = x = x = x = x "
	print "Checking existing build matrix...."
	buildMatrixList = []
	
	#Check buildMatrix here....
	#By finding the values of the subMatrix as it exists in buildMatrix
	print "================ SUB MATRIX ================"
	print "listOfPartHeightMatrix[-1].shape[0]",listOfPartHeightMatrix[-1].shape[0]
	print "listOfPartHeightMatrix[-1].shape[1]",listOfPartHeightMatrix[-1].shape[1]
	subMatrixDimension = int(round((listOfPartHeightMatrix[-1].shape[0]*listOfPartHeightMatrix[-1].shape[1])/2)) # so that you get a single number of the matrix slice 
	print "subMatrixDimension " ,subMatrixDimension
	print "pos [0 - Across] [1 - Down]", pos[0],pos[1] 
	correctionX = pos[0]
	correctionY = pos[1]
	
	subBuildMatrix = buildMatrix[correctionY:correctionY+listOfPartHeightMatrix[-1].shape[0],correctionX:correctionX+listOfPartHeightMatrix[-1].shape[1]] #+2 for a 4x4 brick
	print subBuildMatrix
	
	maxSubBuildMatrix = numpy.amax(subBuildMatrix)
	minSubBuildMatrix = numpy.amin(subBuildMatrix)
	subBuildMatrixTmpList = subBuildMatrix.flatten().tolist()
	
	print "subBuildMatrixTmpList",subBuildMatrixTmpList
	print
	maxSubBuildMatrix = max(subBuildMatrixTmpList)
	correctionValueList = []
	for value in subBuildMatrixTmpList:
		correctionValue = maxSubBuildMatrix - value
		correctionValueList.append(correctionValue)
	print correctionValueList
	
	shapeDimensions = listOfPartHeightMatrix[-1].shape[1]	
	correctionMatrix = numpy.array(correctionValueList).reshape(-1,shapeDimensions) #The 2 here refers to the dimensions of the array - and the brick dimension			
	

	print "*********************************"
	print "correctionMatrix"
	print correctionMatrix
	print "*********************************"
	#Add the correction matrix to the build matrix....
	previousModelMatrix = buildMatrix
	newModelMatrix = correctionMatrix
	buildMatrix = studView.addAtPos(previousModelMatrix, newModelMatrix, pos)
	print "=================== CORRECTED BUILD MATRIX ==================="
	print buildMatrix
	print "============================================"
		
		
	print "============================================"
	print "CALCULATING OVERLAPPING ASSETS"

	buildMatrixList = []
	
	print listOfPartHeightMatrix[-1].shape,listOfPartHeightMatrix[-1][0][0],listOfPartHeightMatrix[-2][0][0]
	partDimensions = listOfPartHeightMatrix[-1].shape[0]*listOfPartHeightMatrix[-1].shape[1]
	print "Calculating height value using...",listOfPartHeightMatrix[-1][0][0],"+",listOfPartHeightMatrix[-2][0][0]
	heightValue = listOfPartHeightMatrix[-1][0][0]+listOfPartHeightMatrix[-2][0][0]
	print
	subBuildMatrix = buildMatrix[correctionY:correctionY+listOfPartHeightMatrix[-1].shape[0],correctionX:correctionX+listOfPartHeightMatrix[-1].shape[1]]
	maxSubBuildMatrix = numpy.amax(subBuildMatrix)
	minSubBuildMatrix = numpy.amin(subBuildMatrix)
	print "Fixing any overlap..."
	if minSubBuildMatrix != maxSubBuildMatrix:
		print "Uneven Sub Matrix - Selecting Max height"
		heightValue = maxSubBuildMatrix
	else:
		heightValue = numpy.amax(subBuildMatrix)
		print "Resetting height to: ",heightValue
	
	print "partDimensions",partDimensions,"heightValue",heightValue
	
	maxValue = heightValue
	

	#Fix overlap here...
	readAndModifyLastLineOfLDRFile(fileName,heightValue,maxValue)
	return buildMatrix

def createPart(part,height,partPath):
	print "CREATING PART"
	
	#SELECT A PART AND GET THE DIMENSIONS
	if part == 0: # For the first part = a base plate set the height to 0
		width = 0
		depth = 0
		colour = 7
		base = True
	else:
		part = 6 #This sets all subsquent parts to a single brick
		part = randint(1,7) #or choose a random part from the list
		base = False

	
	partList = ["41539.dat","3003.dat","3001.dat","3022.dat","3020.dat","3002.dat","3004.dat","3005.dat","3068b.dat"]
	part = partList[part]

	#Analyse selected part to get dimensions...
	LDRAWLocation = "C:\LDraw\Parts\\"
	fullPartPath = LDRAWLocation + part
	print "Full Part Path: ",fullPartPath
	partPath = brickDimensions.BrickCorners(fullPartPath,partPath)
	for analysedPart in partPath:
			localBrickDimensions = brickDimensions.BrickDimensions(analysedPart)
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			print "localBrickDimensions: ",localBrickDimensions
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

			localPartsMatrix.extend(localBrickDimensions)
			print ".......localPartsMatrix: ",localPartsMatrix
			if base: #Set the base part height to 0
				height = 0
			else:
				height = localPartsMatrix[-1][2]*-8
			print "Current Height of Part ",height
		
	#MOVE THE PART TO A LOCATION ON THE BASE	
	if not base:
		width = randint(-2,2)
		depth = randint(-2,2)
		#width = 0 #for testing
		#depth = 0 #for testing
		
		base = False
		print "Location Data W: ",width, " Location Data H: ",depth
	ldr2matOutputForMatrixPos = (width+3,(depth-3)*-1)
	print ldr2matOutputForMatrixPos
	#Change into Lego Units
	width = width*20
	depth = depth*20

	#ROTATE THE PART BY 90 DEGREES IF REQUIRED
	#NO ROTATE 1 4 20 -104 20 0 0 1 0 1 0 -1 0 0 3001.dat
	#90 ROTATE 1 4 20 -104 20 -1 0 0 0 1 0 0 0 -1 3001.dat	
	rotate = randint(0,1)
	if rotate == 1:
		print "*** ROTATING 90 DEGREES ***"
	m1 = 0 
	if rotate == 1:
		m1 = -1
	m2 = 0 
	m3 = 1 
	if rotate == 1:
		m3 = 0
	m4 = 0 
	m5 = 1 
	m6 = 0 
	m7 = -1
	if rotate == 1:
		m7 = 0
	m8 = 0 
	m9 = 0 
	if rotate == 1:
		m9 = -1

	#ADJUST POSTION FOR NON SYMETRICAL PARTS
	#if the width and depth of the part mod 2 != 0 then add 10 to the width
	if localBrickDimensions[0][1] ==1 and localBrickDimensions[0][3] == 1: # EXCLUDE 1x1 bricks as they are symetrical and don't need correcting.
		width = width - 10
		depth = depth + 10
	else: # SPECIAL CASE FOR 1x1 BRICKS
		checkWidth = localBrickDimensions[0][3]
		if checkWidth%2 != 0:
			width = width + 10
			if rotate == 1:
				width = width - 10
				depth = depth-10
				
		checkDepth = localBrickDimensions[0][1]
		if checkDepth%2 != 0:
			depth = depth + 10
			#MAYBE also adjust ldr2matOutputForMatrixPos also as the 2x3 odd shaped bricks shift position by 1 brick
			if rotate == 1:
				depth = depth - 10
				width = width-10

	
	#SET THE COLOUR
	if not base:
		colourHeight = localBrickDimensions[0][2]%20
		colour = colourHeight
		colour = randint(1,9)
	
	ldrLine = [1,colour,width,height,depth,m1,m2,m3,m4,m5,m6,m7,m8,m9,part]
	
	#Check Studs on part
	print
	print "Data for Stud View...",
	print ",".join(str(bit) for bit in localPartsMatrix[-1])
	localPartsMatrixStrForStudView = ",".join(str(bit) for bit in localPartsMatrix[-1])
	print "calling studview here..."
	localPartsStudView = studView.studView(localPartsMatrixStrForStudView,DictionaryOfPartsAndStuds)
	createPartOutput = [ldrLine,localPartsMatrix,localPartsStudView,ldr2matOutputForMatrixPos,rotate,width,depth]
	
	return createPartOutput
	
#Main code	
#How many bricks in the pile?
print
print
print "How many bricks in your pile? - Choose between 1 and 99 "
confirmedBricks = checkInput()

while True:
	
	print "*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^*=^"
	restart = 0
	DictionaryOfPartsAndStuds = {}
	partPath = []
	
	#parts = ['3031.dat','3004.dat','3003.dat','3003.dat','3068b.dat']
	dateTimeStamp = timeStamp()
	
	try:
		fileName = sys.argv[1] + ".ldr"
		renderPath = sys.argv[1]
		fileName = "brickaloRenders//" + renderPath + "//" + fileName
	except:
		fileName = "brickalo_output.ldr"
	
	
	print
	print "fileName: ",fileName
	print
	resetldrFile(fileName)
	height = 0
	ldrLineMatrix = []
	listOfPartHeightMatrix = []
	if restart == 0:
		resetldrFile(fileName)
		for i in range(0,1000):
			print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
			print "LDR Line: ", i+4
			print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
			localPartsMatrix = [] # Reset the local part Matrix (as it scans all the lines in the ldr file)

			ldrLineAndPartsInfo = createPart(i,height,partPath)
			ldrLineAndPartsInfo[0] = activeLineList(ldrLineAndPartsInfo[0])
			fileName = legoWriter(fileName,dateTimeStamp,ldrLineAndPartsInfo[0])
			
			print "-------------------------------------------------"
			print "ldrLineAndPartsInfo[0]: ", ldrLineAndPartsInfo[0]
			print "ldrLineAndPartsInfo[1]: ", ldrLineAndPartsInfo[1]
			print "ldrLineAndPartsInfo[3]: ", ldrLineAndPartsInfo[3]
			print "ldrLineAndPartsInfo[4] - Rotate: ", ldrLineAndPartsInfo[4]
			print "ldrLineAndPartsInfo[5] - Width: ", ldrLineAndPartsInfo[5]
			print "ldrLineAndPartsInfo[6] - Depth: ", ldrLineAndPartsInfo[6]
			print "-------------------------------------------------"
			ldrLineMatrix.append(ldrLineAndPartsInfo[0])
			
			#Analysing File...
			print ".............Analysing local ldr File...................."
			print
			if i == 0:
				print "Base part..."
			else:
				print "Analysing model here..."

			#Clean up data for studView.partHeightMatrix	
			print		
			print "Data for Stud View...",
			#This needs to be the last item in the list ldrLineAndPartsInfo[1]
			print ",".join(str(bit) for bit in ldrLineAndPartsInfo[1][-1]).replace('[','').replace(']','')
			localPartsMatrixStrForPartHeightMatrix = ",".join(str(bit) for bit in ldrLineAndPartsInfo[1][-1]).replace('[','').replace(']','')
			print
			

			print "Model Part for Dictionary:",ldrLineAndPartsInfo[1][i][0]
			print "================ Previous Model Matrix ================"
			print			
			#Initialise the previous model Matrix using the stud view matrix for the first part (should all be 0 with 3031.dat
			if i == 0:
				previousModelMatrix = ldrLineAndPartsInfo[2][ldrLineAndPartsInfo[1][0][0]]
			print "previousModelMatrix: "
			print previousModelMatrix
			print
			print "ldrLineAndPartsInfo[1]: ",ldrLineAndPartsInfo[1]
			print "ldrLineMatrix: ",ldrLineMatrix
			print "ldrLineAndPartsInfo[2]: ",ldrLineAndPartsInfo[2]
			#Get the model matrix now the most recent part has been added to the model...
			print
			print "Calling studView..."
			newModelMatrix = studView.partHeightMatrix(localPartsMatrixStrForPartHeightMatrix)
			if i == 0:
				buildMatrix = newModelMatrix
			print
			print "================ New Model Matrix ================"
			rotate = ldrLineAndPartsInfo[4]
			print ":::::::::::::::::::"
			#Add a Reshape the newModelMatrix for rotation
			matrixReshape = newModelMatrix.shape
			print newModelMatrix
			if i>0 and rotate == 1:
				print "Rotate build matrix...",matrixReshape
				newModelMatrix = newModelMatrix.reshape(int(matrixReshape[1]),int(matrixReshape[0]))
				print
				print newModelMatrix
			forHeightListArray = deepcopy(newModelMatrix)
			print ":::::::::::::::::::"
			print
			listOfPartHeightMatrix.append(forHeightListArray)
			print "================ Current Model Matrix ================" 
			print

			if i > 0:
				print "Values for LDR placement Width: ",ldrLineAndPartsInfo[5]/20, "Depth: ",ldrLineAndPartsInfo[6]/20
				print "Values for Matrix Position",ldrLineAndPartsInfo[3][0],",",ldrLineAndPartsInfo[3][1]
				#Adjust Matrix for brick dimenstions here...
				if "3001" in ldrLineAndPartsInfo[1][-1][0] or "3020" in ldrLineAndPartsInfo[1][-1][0] or ldrLineAndPartsInfo[1][-1][1]%3 == 0:
					
					xPosForAddition = ldrLineAndPartsInfo[3][0]
					yPosForAddition=ldrLineAndPartsInfo[3][1]-1 #Subtract 1 from the y position as the placement at 0,0 is 1 brick off for no symetrical bricks - well 4x2 anyway
					if rotate == 1:
						xPosForAddition = ldrLineAndPartsInfo[3][0]-1
						yPosForAddition=ldrLineAndPartsInfo[3][1]
				elif "3004" in ldrLineAndPartsInfo[1][-1][0]:
					
					xPosForAddition = ldrLineAndPartsInfo[3][0]+1
					yPosForAddition=ldrLineAndPartsInfo[3][1]
					if rotate == 1:
						xPosForAddition = ldrLineAndPartsInfo[3][0]
						yPosForAddition=ldrLineAndPartsInfo[3][1]+1
				else:	
					xPosForAddition = ldrLineAndPartsInfo[3][0]
					yPosForAddition = ldrLineAndPartsInfo[3][1]
				
				pos = (xPosForAddition,yPosForAddition)
				
				buildMatrix = studView.addAtPos(previousModelMatrix, newModelMatrix, pos)
				print "ooooooooooooooooo BUILD MATRIX ooooooooooooooooo"
				print buildMatrix
				buildMatrix = checkBuildMatix(buildMatrix,listOfPartHeightMatrix,ldrLineAndPartsInfo,pos)
				print "===================== BUILD MATRIX CROSS CHECK ====================="
				print buildMatrix
				
			print 
			
			
			previousModelMatrix = buildMatrix
			
			print "===================== PREVIOUS BUILD MATRIX CROSS CHECK ====================="
			print previousModelMatrix
			print
			print "ADDING ANOTHER PART..."
			
			
			if i == confirmedBricks:
				print 
				if confirmedBricks > 1:
					print "We're all done - Your file 'brickalo_output.ldr' containing", confirmedBricks, "bricks is ready..."
				else:
					print "We're all done - Your file 'brickalo_output.ldr' containing", confirmedBricks, "brick is ready..."
				raw_input ("Press Enter to exit...")
				sys.exit(0)
				if quit == "Q" or quit == "q":
					print 
					raw_input ("Press Enter to exit...")
					sys.exit(0)
				else:
					restart = 1
					break				
print "================================="
print
