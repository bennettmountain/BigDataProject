from PIL import Image, ImageDraw

highHeel = Image.open('high_heel.jpg')


width, height = highHeel.size


endPoints = [(395, 210), (250, 340)]

draw = ImageDraw.Draw(highHeel)
draw.line(endPoints, fill='red')
highHeel.save('try1.png')

firsty = Image.open('try1.png')
firsty.show()

def drawLines(points, numLines):
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
		# shift the point on the bottom of the image left
		# shift the point on the side of the image down
		rightPtY += 3
	#	leftPtX += 10

		ends = [(rightPtX, rightPtY), (leftPtX, leftPtY)]
		draw.line(ends, fill='red')
		tryi_string = 'try' + str(i) + '.png'
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
	firsty = Image.open('try2.png')
	firsty.show()
drawLines(endPoints,100)



