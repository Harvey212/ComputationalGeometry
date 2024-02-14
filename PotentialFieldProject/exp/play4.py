from tkinter import *
import numpy as np
import math
from math import sin, cos, radians 



c = Canvas(width=200, height=200)
c.pack()

# a square
xy = [(50, 50), (150, 50), (150, 150), (50, 150)]

polygon_item = c.create_polygon(xy)


cxx=(50+150+150+50)/4

cyy=(50+50+150+150)/4


center =[cxx,cyy]

def getangle(ss):

	sx=ss[0]
	sy=ss[1]


	dx = sx - center[0]
	dy = sy - center[1]



	#dx = c.canvasx(event.x) - center[0]
	#dy = c.canvasy(event.y) - center[1]
	try:
		return complex(dx, dy) / abs(complex(dx, dy))
	except ZeroDivisionError:
		return 0.0 # cannot determine angle

#def press(event):
    # calculate angle at start point
#	global start
#	start = getangle(event)



def motion(event):


	p1=[50,50]
	start=getangle(p1)


	# calculate current angle relative to initial angle
	#global start

	p2=rotate_point(p1, 60, center)


	angle = getangle(p2) / start


	offset = complex(center[0], center[1])
	newxy = []
	for x, y in xy:
		v = angle * (complex(x, y) - offset) + offset
		newxy.append(v.real)
		newxy.append(v.imag)
	c.coords(polygon_item, *newxy)


def rotate_point(point, angle, center_point):
	
	angle_rad = radians(angle % 360)
	# Shift the point so that center_point becomes the origin
	vec = (point[0] - center_point[0], point[1] - center_point[1])
	new_point = (vec[0] * cos(angle_rad) - vec[1] * sin(angle_rad),
	vec[0] * sin(angle_rad) + vec[1] * cos(angle_rad))
	# Reverse the shifting we have done
	fnew_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
		
	ffnew_point=list(fnew_point)

	return ffnew_point


c.bind("<Button-1>", motion)
#c.bind("<B1-Motion>", motion)

mainloop()