import numpy
from PIL import Image, ImageDraw

def drawLines(points, numLines):
	global fileIndex
	
	"""
	shifts the two endpoints and draws numLines lines on the image, 
	visualizing possible breaks
	points: list of two tuples containing the point on the right edge and bottom
			edge which serve as the endpoints of the original line
	"""
	draw = ImageDraw.Draw(highHeel)
	#rightX and bottomY coordinates stay constant
	rightPtX, rightPtY = points[0][0], points[0][1]
	leftPtX, leftPtY = points[1][0], points[1][1]

	for i in list(range(1, numLines+1)):
		# shift the point on the top right down
		rightPtY += 1

		ends = [(rightPtX, rightPtY), (leftPtX, leftPtY)]
		draw.line(ends, fill='red')
		tryi_string = 'try/' + 'try' + str(fileIndex) + '.png'
		tryi = Image.open('high_heel.jpg')
		draw = ImageDraw.Draw(tryi)
		tiwidth,tiheight = tryi.size
		highHeel.save(tryi_string)
		for j in range(tiwidth) :
			for k in range(tiheight):
				point = [(j,k)]
				distance = (j - leftPtX)*(rightPtY - leftPtY) - (k - leftPtY)*(rightPtX - leftPtX)
				if distance < 0:
					draw.point(point,fill='white')
		tryi.save(tryi_string)
		fileIndex += 1

def drawStrongLines(numIters, starting, length, width):
	global file2Index
	
	
	#rightX and bottomY coordinates stay constant
	# 359-380 x, 280 y
	
	leftPtY = starting[1] - 1
	
	for i in list(range(1, numIters + 1)):
		leftPtX = int(starting[0] - 40/i) 
		endPtX = leftPtX + 10 
		tryi = highHeel.copy()
		tiwidth,tiheight = tryi.size
		draw = ImageDraw.Draw(tryi)
		leftPtY -= 1
		tryi_string = 'Newtry/' + 'try' + str(file2Index) + '.png'
		
		firstpoints = [(leftPtX, leftPtY), (endPtX, leftPtY)]
		draw.line(firstpoints,fill = 'red')
		for k in list(range(leftPtY, tiheight)):
			for j in list(range(leftPtX,endPtX)):
				point = [(j,k)]
				#draw.point(point,fill='white')

		verticalendPtY = leftPtY + length
		firstVertPoints = [(endPtX,leftPtY), (endPtX,verticalendPtY)]
		draw.line(firstVertPoints, fill = 'red')
		
		wide = int(width + (4.5*i/numTries) + ((8*i/numTries)/numTries)) 
		horEndPtX = endPtX + wide
		horPoints = [(endPtX,verticalendPtY), (horEndPtX, verticalendPtY)]
		draw.line(horPoints, fill = 'red')
		for k in list(range(verticalendPtY, tiheight)):
			for j in list(range(endPtX,horEndPtX)):
				point = [(j,k)]
				#draw.point(point,fill='white')

		vertical2endPtY = verticalendPtY - length
		secondVertPoints = [(horEndPtX, verticalendPtY),(horEndPtX,vertical2endPtY)]
		draw.line(secondVertPoints, fill = 'red')

		finalPoints = [(horEndPtX,vertical2endPtY), (tiwidth, vertical2endPtY)]
		draw.line(finalPoints, fill = 'red')
		for k in list(range(vertical2endPtY, tiheight)):
			for j in list(range(horEndPtX,tiwidth)):
				point = [(j,k)]
				#draw.point(point,fill='white')


		tryi.save(tryi_string)
		file2Index += 1




def createDiffs(numTries):
	for i in range(numTries):
		
		highHeel = Image.open('high_heel.jpg')
		width, height = highHeel.size

		tryi_string = 'try/' +'try' + str(i + 1) + '.png'
		tryi = Image.open(tryi_string)

		diff_string = 'diff/' + 'diff' + str(i + 1) + '.png'
		diffImage = Image.new('RGB', (width, height))
		
		for x in range(width):
			for y in range(height):
				point = (x,y)
				highHeelRGBValue = highHeel.getpixel(point)
				tryiRGBValue = tryi.getpixel(point)
				diff = tuple(numpy.subtract(tryiRGBValue,highHeelRGBValue))
				
				invdiff = tuple(numpy.subtract((255,255,255), diff))
				diffImage.putpixel(point,invdiff)
		diffImage.save(diff_string)

fileIndex = 1
file2Index = 1
highHeel = Image.open('high_heel.jpg')
width, height = highHeel.size
endPoints = [(395, 210), (250, 350)]
starting = [353, 350]
numTries = 170
numIters = 10
drawStrongLines(numTries, starting, 6, 5)
drawStrongLines(numTries, starting, 8, 4)
drawStrongLines(numTries, starting, 10, 4)
drawStrongLines(numTries, starting, 12, 2)
drawStrongLines(numTries, starting, 4, 4)
#createDiffs(numTries * numIters)

