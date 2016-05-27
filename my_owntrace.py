import cv2
import numpy as np
temp = cv2.imread('finger.png',0)
w,h = temp.shape[::-1]
cap = cv2.VideoCapture(0)



i = 0
black = np.zeros((480,640,3), np.uint8)
black1 = np.zeros((480,640,3), np.uint8)
while(True):

	ret, frame = cap.read()
	
	framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	method = eval('cv2.TM_CCOEFF_NORMED')
	res = cv2.matchTemplate(framegray,temp,method)
	min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)


	if max_val>0.82:
		cv2.rectangle(frame,top_left,bottom_right,255,2)
	'''print max_val'''
	origin = (top_left[0] + w/2,top_left[1] + h/2) 
	point1 = origin
	if max_val>0.82 and i > 0 and point1 != point2:
		cv2.circle(black,(origin),4,(0,0,255),-1)
		cv2.line(black1,point1,point2,(0,0,255),5)
	cv2.imshow('dots',cv2.flip(black,1))
	cv2.imshow('line',cv2.flip(black1,1))

	'''cv2.imshow('frame',frame)'''

	if cv2.waitKey(1) == ord('r'):
		black = np.zeros((480,640,3), np.uint8)
		black1 = np.zeros((480,640,3), np.uint8)
	point2 = origin
	
	i += 1
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()
	

