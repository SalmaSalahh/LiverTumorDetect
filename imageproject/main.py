import cv2
import numpy as np
from statistics import stdev


#read image

# Liver with Tumor
# img_raw = cv2.imread("tumor1.jpeg")
# img_raw = cv2.imread("1.jpg")
# img_raw = cv2.imread("3.png")
# img_raw = cv2.imread("6jpg.jpg")
# img_raw = cv2.imread("Nh2.jpg")
# img_raw = cv2.imread("N3.png")

# Healthy Liver
img_raw = cv2.imread("h1.jpg")
# img_raw = cv2.imread("h2.gif")
# img_raw = cv2.imread("h3.jpeg")
# img_raw = cv2.imread("Nh3.png")

#select ROI function
roi = cv2.selectROI(img_raw)

#print rectangle points of selected roi
print(roi)

#Crop selected roi from raw image
roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#show cropped image
cv2.imshow("ROI", roi_cropped)

#To save an image
cv2.imwrite("crop.jpeg",roi_cropped)

#hold window
cv2.waitKey(0)

dimensions = roi_cropped.shape
row = roi_cropped.shape[0]
col = roi_cropped.shape[1]
print (row)
print (col)
print('The Shape of the image is:',roi_cropped.shape)
print('The image as array is:')
print(roi_cropped)
standardDeviation = np.std(roi_cropped)
print(standardDeviation)

if (standardDeviation>=16):
    print('Liver with Tumor.')
elif (standardDeviation<16):
    print('Healthy Liver.')