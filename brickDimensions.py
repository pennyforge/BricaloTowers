import os.path
from easygui import *

'''
def call_fileopenbox():
	msg = "LDR file"
	title = "Open file"
	default = "C:\\Users\Neil\\Google Drive\\Lego_OnGDrive\\Code"
	filetypes = ["*.ldr","*.pov","All files","*"]
	f = fileopenbox(msg, title, default, filetypes)
	print("You chose to open file: {}".format(f))
	filePath = f
	return filePath
'''

def splitsting(line,item):
	SplitLine = line.split()
	datFile = SplitLine[item]
	return datFile

def CountCorners(partName):
	print "PART ID: ",partName
	with open(partName) as f:
		lines = f.readlines()		
	for line in lines:
		if line[0] == "4":
			firstCorner = int(splitsting(line,2))
			#print "Found line starting with 4",
			#print " mod>>>", firstCorner % 10
			if firstCorner % 10 == 0:
				#print "Found line starting with 4 and whole number placement",line
				#print "Add 1 to countCorners"
				countCorners = countCorners + 1
				#print "CountCorners: ", countCorners
			if countCorners == 4:
				break
		try:
			if countCorners == 4:
				print "FOUND 4 CORNERS"
		except:
			countCorners = 0
	return countCorners
	
def BrickCorners(FileName,partPath):
	print "********** PROCESSING PART **********"
	corners = CountCorners(FileName)
	if ".dat" in FileName:
		datFile = os.path.basename(FileName)
		print ".dat File Name: ", datFile
	print "Corners = ",corners
	print
	if corners == 4:
		print "Found 4 corners in ", FileName 
		print "Moving to next part..."
		#print "*****************************************************"
		print
		partPath.append(FileName)
		with open(FileName) as f:
			lines = f.readlines()		
			#Add the corner data to an array
			#Calculate the dimensions of the brick
			for line in lines:
				if line[0] == "4":
					#print "line[0] ", line[0]
					break
	else:
		if ".ldr" in FileName:
			print "Analysing LDR file..."
		else:
			print "Unable to find enough corners in ", FileName,"...going deeper..."
		#print "==================================================="
		#print
		with open(FileName) as f:
			lines = f.readlines()		
			for line in lines:
				if line[0] == "1" and ".dat" in line:		
					datFile = splitsting(line,14)
					pathToDat = LDRAWLocation + datFile 
					if os.path.isfile(pathToDat): 
						partPath = BrickCorners(pathToDat,partPath)		
	return partPath		

'''
def calculateMaxMin(countCorners,line,lineItem,dimType):	
	if countCorners == 1:
		firstCorner = int(splitsting(line,lineItem))
		maxValue = firstCorner
		minValue = firstCorner
	elif countCorners == 2:	
		secondCorner = int(splitsting(line,lineItem))
		maxValue = max(firstCorner,secondCorner)
		minValue = min(firstCorner,secondCorner)
	elif countCorners == 3:
		thirdCorner = int(splitsting(line,lineItem))
		maxValue = max(firstCorner,secondCorner,thirdCorner)
		minValue = min(firstCorner,secondCorner,thirdCorner)
	elif countCorners == 4:
		forthCorner = int(splitsting(line,lineItem))
		maxValue = max(firstCorner,secondCorner,thirdCorner,forthCorner)
		minValue = min(firstCorner,secondCorner,thirdCorner,forthCorner)
	Dimension = (maxValue-minValue)/dimType
	print "Dimension: ", Dimension
	return Dimension
'''

def SearchForStuds(FileName, StudCount):	
	with open(FileName) as f:
		lines = f.readlines()		
	for line in lines:
		#print line[0]
		if line[0] == "1":
			#print line
			if "stud.dat" in line:
				StudCount = StudCount + 1 
				#print "*** FOUND STUD***", StudCount
				#print 
				
			elif ".dat" in line:
				datFile = splitsting(line,14)
				pathToDat = LDRAWLocation + datFile 
				#print pathToDat, StudCount
				if os.path.isfile(pathToDat): 
					StudCount = SearchForStuds(pathToDat,StudCount)
	#print
	return StudCount		


def BrickDimensions(FileName):
	print "************* FINDING DIMENSIONS FOR..."
	print "PART ID: ",FileName
	Width = 0
	Height = 0
	Depth = 0
	Dimension = 0
	DimensionList = []
	singlePartMatrix = []
	with open(FileName) as f:
		lines = f.readlines()		
	for line in lines:
		#print line[0]
		if line[0] == "4":
			firstCorner = int(splitsting(line,2))
			#print "Found line starting with 4",
			#print " mod>>>", firstCorner % 10
			if firstCorner % 10 == 0:
				#print "Searching for Quads...Found line starting with 4 and whole number placement",line
				#print "Add 1 to countCorners"
				countCorners = countCorners + 1
				#print "CountCorners: ", countCorners

				DimensionList.extend([int(splitsting(line,2)),int(splitsting(line,3)),int(splitsting(line,4))]) 
							
			if countCorners == 4:
				maxDValue = max(DimensionList[0],DimensionList[3],DimensionList[6],DimensionList[9])
				minDValue = min(DimensionList[0],DimensionList[3],DimensionList[6],DimensionList[9])
				maxHValue = max(DimensionList[1],DimensionList[4],DimensionList[7],DimensionList[10])
				minHValue = min(DimensionList[1],DimensionList[4],DimensionList[7],DimensionList[10])
				maxWValue = max(DimensionList[2],DimensionList[5],DimensionList[8],DimensionList[11])
				minWValue = min(DimensionList[2],DimensionList[5],DimensionList[8],DimensionList[11])
				Depth = (maxDValue - minDValue)/20
				Height = maxHValue/8
				#print "maxHValue: ",maxHValue
				Width = (maxWValue - minWValue)/20
				if maxHValue % 8 == 0:
					Studs = 1 # Part has studs
					print "Part has studs"
				else:
					if maxHValue == 7 or maxHValue == 15 or maxHValue == 23:
						Height = 1
					Studs = 0 # Part is studless
					print "Part is studless"

				if Studs == 1:
					StudsAvailable = "Yes"
				else:
					StudsAvailable = "No"
				#print "DimensionList: ", DimensionList

				#================================
				StudCount = 0
				StudCount = SearchForStuds(FileName, StudCount)
				#================================				
				
				#print
				print "PART DETAILS: ",FileName, " Depth: ",Depth, " Height: ", Height, " Width: ",Width, " Studs Available: ", StudsAvailable, " Nos Of Studs: ", StudCount
				singlePartMatrix.append([FileName,Depth,Height,Width,Studs,StudCount])
				#print
				break
		try:
			if countCorners == 4:
				print "FOUND 4 CORNERS"
		except:
			countCorners = 0
	return singlePartMatrix



	
LDRAWLocation = "C:\LDraw\Parts\\"	

if __name__ == "__main__":
	partPath = []
	
	print "...being run directly"
	#FileName = call_fileopenbox()
	FileName = "C:\\Users\Neil\\Google Drive\\Lego_OnGDrive\\Code\\DetectStuds\\2Bricks_4x4_2x2Plate.ldr"

	partPath = BrickCorners(FileName,partPath)	
	print "Corner analysis complete"
	#print "partPath...",partPath
	print
	print "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
	print
	partsMatrix=[]
	print "Constructing parts matrix using...",partPath
	for part in partPath:
		brickDimensions = BrickDimensions(part)
		partsMatrix.extend(brickDimensions)
		
	#print partsMatrix

else:
    print("...being imported into another module")

	
	
