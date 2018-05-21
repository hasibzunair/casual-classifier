# casual-classifier-KNN-BFMatch

Here, a flann based knn matcher using sift feature extractor and brute force matching is demonstrated using the training image/ template as the jackfruit.The key points and their descriptors are found using the orb detector. Different images of fruits are given as an input and the output is shown as a result of good matches. From both the algorithms, the features are extracted and the result is stored in the matches/goodmatch variable of each technique. 


# Dependencies 

I have used the following dependencies.

   * openCV
   * matplotlib
   * numpy
   * math
   
# Template

For the training image for KNN and the template for BFMatcher I have used this image. <br />

![alt-text-2](https://github.com/hasibzunair/strawberry-detector/blob/master/Figure_2.png "title-2")<br />
 
# Results

For the KNN matcher the minimum match count is 195 and for the brute force matcher it is 10. Below are the results for different input images which show the match score.

Flann Based KNN Matcher             |  Brute Force Matcher
:-------------------------:|:-------------------------:
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_1.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_1.png) 
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_2.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_2.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_3.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_3.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_4.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_4.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_5.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_6.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_6.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_6.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_7.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_7.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_8.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_8.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_9.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_9.png)
![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/knn/Figure_10.png) |  ![](https://github.com/hasibzunair/casual-classifier-KNN-BFMatch/blob/master/bfMatch/Figure_10.png)   

# Credits



