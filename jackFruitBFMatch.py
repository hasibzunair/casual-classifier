import cv2
import numpy as np
import matplotlib.pyplot as plt


MIN_MATCH_COUNT = 195

img1 = cv2.imread('test_images/train.png')
img2 = cv2.imread('test_images/10.png')

img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

if(len(matches)> MIN_MATCH_COUNT ):
    print("Jackfruit Detected")

else:
    print("Not Enough match found- %d %d" % (len(matches), MIN_MATCH_COUNT))

x = len(matches)
y = 'Matches Score =  '
z = y + str(x)

plt.figure(1)
plt.suptitle('Jackfruit Classifier using Brute Force Matcher', fontsize=16)
plt.plot(1)
plt.xlabel(z)
plt.imshow(img2_rgb)
plt.show()

