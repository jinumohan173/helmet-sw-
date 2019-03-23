#author : Jinu Mohan
#DOC    : 23/03/2019
#Toc    : 1:20 pm

import cv2
import numpy as np
import time
import os



def min_max_x_y(contour):
	min_x=9999
	min_y=9999
	max_x=-9999
	max_y=-9999
	for [[x,y]] in contour:
		if(x<min_x):
			min_x=x
		if(y<min_y):
			min_y=y
		if(x>max_x):
			max_x=x
		if(y>max_y):
			max_y=y
	return min_x,min_y,max_x,max_y

def abs(x):
	if x<0:x*=-1
	return x

def count_transitions(image,min_x,min_y,max_x,max_y):
	mid_y=(min_y+max_y)/2
	count=0
	for i in range(min_x,max_x):
		print i,mid_y
		if(abs(int(image[i,mid_y][0]-image[i+1,mid_y][0]))>=200):
			count+=1

	return count

def pattern_detection(user):
	count = 0
	cap = cv2.VideoCapture(0)
	entered=0
	t1=time.time()
	while(cap.isOpened()):
		ret,frame=cap.read()
		if(ret==False):break
		frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.bilateralFilter(gray,11,17,17)
		edge_image=cv2.Canny(gray,30,200)
		blurred=cv2.blur(edge_image,(9,9))
		
		result = cv2.findContours(edge_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		contours, h= result if len(result) == 2 else result[1:3]
		
		if entered==0 or time.time()-t1>=5.0:
			t1=time.time()
			flag=0
		if user==1:
			largest_area=0.0
			index=-1
			for i in range(len(contours)):
				approx=cv2.approxPolyDP(contours[i],0.01*cv2.arcLength(contours[i],True),True)
				if len(approx)==4:
					a=cv2.contourArea(contours[i],False)
					if(a>largest_area and a>=10.0):
						largest_area=a
						index=i
			if(index!=-1 and largest_area>=20):
				min_x,min_y,max_x,max_y=min_max_x_y(contours[index])
				c=count_transitions(frame,min_x,min_y,max_x,max_y)/3
				if(c>=5 and c<=15):
					flag=1
					cv2.rectangle(frame,(min_x,min_y),(max_x,max_y),(0,255,0),2)
			if flag==0:
				print ("You are not wearing a helmet$$$$$$")
				count = 0
				print(count)
			else:				
				count = count+1
				print(count)
			if(count == 10):
				
				print("helmet found theft#####")
				cap.release()
				os.system("sudo fswebcam -r 640x480  -S 10 /var/www/html/image2.jpg")
		cv2.imshow('Edge Image',edge_image)
		cv2.imshow('Detected',frame)
		entered=1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
	

while 1:
	try:
		pattern_detection(1)
	except IndexError:
		#cap.release()
		print("  ")
	
def Helmet_Rider():
	pattern_detector(1)

