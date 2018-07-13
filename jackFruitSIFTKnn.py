import cv2
from matplotlib import pyplot as plt
import numpy as np

MIN_MATCH_COUNT = 10
detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDITREE = 0
flannParam = dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann = cv2.FlannBasedMatcher(flannParam, {})

trainImg = cv2.imread("test_images/train.png",0)
trainKP, trainDesc = detector.detectAndCompute(trainImg,None)

test_image = cv2.imread("test_images/5.png")
test_image_rgb = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)

QueryImg = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
queryKP, queryDesc = detector.detectAndCompute(QueryImg,None)
matches = flann.knnMatch(queryDesc, trainDesc, k=2)

goodMatch=[]
for m,n in matches:
    if(m.distance < 0.75*n.distance):
            goodMatch.append(m)

if(len(goodMatch) > MIN_MATCH_COUNT):
    tp = []
    qp = []
    print("JackFruit Detected")

    for m in goodMatch:
        tp.append(trainKP[m.trainIdx].pt)
        qp.append(queryKP[m.queryIdx].pt)
    tp, qp = np.float32((tp, qp))

    H, status = cv2.findHomography(tp, qp, cv2.RANSAC, 3.0)

    h, w = trainImg.shape
    trainBorder = np.float32([[[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]])
    queryBorder = cv2.perspectiveTransform(trainBorder, H)
    cv2.polylines(test_image, [np.int32(queryBorder)], True, (0, 255, 0), 5)
else:
    print("Not Enough match found- %d %d" %(len(goodMatch), MIN_MATCH_COUNT))

x = len(goodMatch)
y = 'Matches Score =  '
z = y + str(x)
# display the results
plt.figure(1)
plt.suptitle('Jackfruit Classifier using FLANN based KNN Matcher', fontsize=16)
plt.plot(1)
plt.xlabel(z)
plt.imshow(test_image_rgb)
plt.show()
