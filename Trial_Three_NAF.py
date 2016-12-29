# Nutrient (N)

from __future__ import division
import cv2
#import time
from datetime import datetime
import numpy as np
#import matplotlib.pyplot as plt

# Nutrient
# ----------------------------------------------------------------------------------------------------------------------------------------------------

H_x_1 = cv2.imread('D:\\CLG\\STUDY\\TCS_Internship_Related\\Grow_Phase\\Testing_&_Calibration\\Hemocheck\\Moto_G4_Plus\\HB_Shashi (1).jpg')


# Fit image to screen
screen_res = 1280, 720
scale_width = screen_res[0] / H_x_1.shape[1]
scale_height = screen_res[1] / H_x_1.shape[0]
scale = min(scale_width, scale_height)
window_width = int(H_x_1.shape[1] * scale)
window_height = int(H_x_1.shape[0] * scale)

cv2.namedWindow('Nutrient', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Nutrient', window_width, window_height)

# Avg of 'R' value
H_x_Gray = H_x_1[2500:2550, 1200:1250, 2]  # Store values of each and every pixel in an array
print H_x_Gray    # Print the array

# Draw rectangle
cv2.rectangle(H_x_1, (1200, 2500), (1250, 2550), (0,255,0), 2)
cv2.imshow('Nutrient', H_x_1)


Gray = np.sum(H_x_Gray) # Summation of all the pixel values

G_Avg = Gray / 2500.0    # Average

N = int(G_Avg) # Convert into integer


print "N value is"
print N

filename = "D:\\CLG\\STUDY\\TCS_Internship_Related\\Grow_Phase\\Testing_&_Calibration\\Hemocheck\\HB_14\\Trial_One_HB-%s_GS=%i.jpg"%(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),  N)
cv2.imwrite(filename,H_x_1)


#camera.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
