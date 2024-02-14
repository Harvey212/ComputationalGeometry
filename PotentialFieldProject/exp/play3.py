import tkinter as tk
import math
from math import sin, cos, radians 
import numpy as np
from skimage.draw import polygon 



class Item():

	def __init__(self, canvas, items):

		self.previous_x = None
		self.previous_y = None
		self.selected = None

		self.items = items
		self.bitmap=np.zeros((fullwindow,fullwindow))

		for item in self.items:
			canvas.tag_bind(item, '<ButtonPress-1>',   lambda event, tag=item: self.on_press_tag(event, tag))
			canvas.tag_bind(item, '<ButtonRelease-1>', lambda event, tag=item: self.on_release_tag(event, tag, self.items))
			canvas.tag_bind(item, '<B1-Motion>', self.on_move_tag)
			


	def on_press_tag(self, event, tag):
		self.selected = True
		self.previous_x = event.x
		self.previous_y = event.y

		print('press:', event, tag)

	def on_release_tag(self, event, tag, itemm):
		self.selected = False
		self.previous_x = None
		self.previous_y = None

		print('release:', event)


		for i in itemm:
			print(canvas.coords(i))
		#print('release:', event.x)
		#print('release:', event.y)

	def on_move_tag(self, event):
		#print(event.x, event.x)
		if self.selected:
			dx = event.x - self.previous_x
			dy = event.y - self.previous_y

			for item in self.items:
				canvas.move(item, dx, dy)
			self.previous_x = event.x
			self.previous_y = event.y
	



###############################################
def rotate_point(point, angle, center_point=(0, 0)):
	"""Rotates a point around center_point(origin by default)
	Angle is in degrees.
	Rotation is counter-clockwise
	"""
	angle_rad = radians(angle % 360)
	# Shift the point so that center_point becomes the origin
	vec = (point[0] - center_point[0], point[1] - center_point[1])

	new_point = (vec[0] * cos(angle_rad) - vec[1] * sin(angle_rad),
		vec[0] * sin(angle_rad) + vec[1] * cos(angle_rad))


    # Reverse the shifting we have done
	res = (new_point[0] + center_point[0], new_point[1] + center_point[1])
	
	return res


def rotate_polygon(polygon, angle, center_point=(0, 0)):
	"""Rotates the given polygon which consists of corners represented as (x,y)
	around center_point (origin by default)
	Rotation is counter-clockwise
	Angle is in degrees
	"""
	rotated_polygon = []
	for corner in polygon:
		rotated_corner = rotate_point(corner, angle, center_point)

		rotated_polygon.append(rotated_corner)
	
	return rotated_polygon



def world_2_canvas(world):
	
	world=list(world)
	can=[]
	tr=0
	count=0
	for num in world:
		check=count%2
		if check==0:
			tr=num+halfwindow
		else:
			tr=halfwindow-num

		can.append(tr)
		count=count+1

	return can



halfwindow=200
fullwindow=halfwindow*2


root = tk.Tk()
canvas = tk.Canvas(root,width=fullwindow,height=fullwindow)
canvas.grid(row=0,column=0)
canvas.pack()

t1=(17, 6, -17, 6, -17, -7, 25, -7)

count=0
cx=0
cy=0

check=[]

for i in range(0,8):
	if (count%2)==0:
		tem=[]
		cx=cx+t1[i]
		tem.append(t1[i])
	else:
		cy=cy+t1[i]
		tem.append(t1[i])
		check.append(tem)

	count=count+1

cx=cx/4
cy=cy/4

test=rotate_polygon(check, 60,(cx,cy))



ff=[]

for i in test:
	xx=i[0]
	yy=i[1]
	ff.append(xx)
	ff.append(yy)

p2=world_2_canvas(ff)

p1=world_2_canvas(t1)

jo=tuple(p2)





sasa=(0, 50, 0, 200, 50, 200, 50, 50)


items = [
		canvas.create_polygon(sasa , fill="blue"),
      ]
Item(canvas, items)


root.mainloop()			

#######################################################3


























#t3=(9, -3, 9, 6, -11, 6, -11, -3)
#t4=(1, 6, 1, 10, -2, 10, -2, 6)

#p3=world_2_canvas(t3)
#p4=world_2_canvas(t4)

#items = [
#		canvas.create_polygon(p3 , fill="blue"),
#		canvas.create_polygon(p4 , fill="blue"),
#      ]
#Item(canvas, items)


###########################################################

#items = [
#		canvas.create_polygon((17, 6, -17, 6, -17, -7, 25, -7) , fill="blue"),
#      ]
#Item(canvas, items)


##################################################################
#items = [
#			canvas.create_polygon((300,  60, 320,  80, 340,  60, 320, 20), fill='green'),
#			canvas.create_rectangle((310, 80, 330, 100), fill='red', width=0),
#			canvas.create_polygon((300, 120, 320, 100, 340, 120), fill='green'),
#]
#Item(canvas, items)


################################################################3

#canvas.create_oval((100, 80, 120, 100), fill='green'),
#canvas.create_rectangle((100, 120, 120, 140), fill="red"),

#canvas.create_polygon((9, -3, 9, 6, -11, 6, -11, -3), fill="blue"),
#canvas.create_polygon((1, 6, 1, 10, -2, 10, -2, 6), fill="red"),	

#canvas.create_polygon((9, -3, 9, 6, -11, 6, -11, -3), fill="red"),




###############################################################################
#t1=(9, -7, 13, 0, 9, 6, -11, 6, -14, 0, -11, -7)
#p1=world_2_canvas(t1)

#items = [
#		canvas.create_polygon(p1 , fill="blue"),
#      ]
#Item(canvas, items)

########################################################

#my_polygon = [(-10, 0), (10, 0), (0, 10)]



#check=[]

#for i in range(0,len(my_polygon)):
#	sw=world_2_canvas(my_polygon[i])
#	check.append(sw)


############################################

#lala=[]


#cx=0

#cy=0

#for i in range(0,len(check)):
#	p1=check[i]
#	x1=p1[0]
#	y1=p1[1]
#	lala.append(x1)
#	lala.append(y1)

#	cx=cx+x1
#	cy=cy+y1

#t1=tuple(lala)


#cx=cx/3

#cy=cy/3
#################################


#########################################3
#test=rotate_polygon(check, 30,(cx,cy))

#gg=[]

#for i in range(0,len(test)):
#	pp=test[i]
#	xx=pp[0]
#	yy=pp[1]
#	gg.append(xx)
#	gg.append(yy)

#t2=tuple(gg)


########################################################
#print(tt)



#print((test[0])[0])

######################################33

###############################
#img = np.zeros((10, 10))

#r = np.array([1, 2, 8, 0])
#c = np.array([1, 7, 4, 0])

#rr, cc = polygon(r, c)

#img[rr, cc] = 1

#print(img)




####################################################