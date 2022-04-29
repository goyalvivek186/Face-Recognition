#CV2 = computer vision-> Images, Video 
#Os = System library-> system Cmd working
#PIL = Pillow lib-> Image processing

import cv2,os
import numpy as np
from PIL import Image

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

max_count = 50

Id = int(input("Enter your Id "))
s = ''
flag = False
r = open("Mapping.txt",'r')

for a in r.read():
	if flag == True and a == '\n':
		break
	if flag == True and a!=' ':
		s = s + a	#read namme
	if a == str(Id):
		flag = True
r.close()
#s = name

while True:
	Name = input("Enter your name ")
	if flag == False:
		break
	if flag == True and Name == s:
		break

if flag == False:
	w = open("Mapping.txt",'a')
	w.write(str(Id)+"  "+Name+"\n")
	w.close()

low = 0
if flag == True:		#If name and ID already exist = Same person again
	imgs = os.listdir('dataSet')	#images = array of names
	low = -1
	for img in imgs:
		print (img)
		n = int(img.split(".")[1])
		print (n)
		if n == Id:
			print ("Hello")
			x = int(img.split(".")[2])
			print (x)
			if x>low:
				low = x	#Low = max

print (low)
sampleNum = low
print (sampleNum)
count = 0

#capture images 
#more 50 if already exists
while(True):
	ret,img=cam.read()
	#ret = true/false => Image got or not
	#img = image matrix
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	#conver to gray scale
	faces = detector.detectMultiScale(gray,1.3,5) 
	#faces = cordinates of rect
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		sampleNum = sampleNum + 1
		count = count + 1
		print (sampleNum)
		cv2.imwrite("dataSet/"+Name+"."+str(Id)+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
		#Right top, Bottom left cordinates of image
		cv2.imshow('frame',img)
	if (cv2.waitKey(100)  == ord('q') or cv2.waitKey(100)  ==  ord('Q')):
		print("Exitted")
		break
	elif count > max_count:
		break

cam.release()
cv2.destroyAllWindows()

import trainer
