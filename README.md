# Smart Social Distancing Enforcement System

COVID 19 is disrupting life-saving immunization services around the world, putting millions of children  in rich and poor countries. During this pandemic, people are adviced to not be in close contact with others to reduce the spread of the disease. But there are still many humans who are negligent about this disease by not maintaining social distance. So, I developed this project to monitor if people are maintaining social distance or not.

Webcam is used to capture the video and detect people in real-time. If people are very close to each other, a red bounding box is displayed around them indicating that they are not maintainting social distance.

<br/><br/>

# How we Detect the Distance between two Objects

We use MobileNet SSD model which can detect 20 diifferet objects. The list of objects that can be detected can be found in the [class_labels.txt](class_labels.txt) file. You can also load any pre-trained model from Deep Learning frameworks like Caffe, Tensorflow, Torch and Darknet.

<br/><br/>

## First we find the focal length of the Camera

To detect the distance of people from camera, triangle similarity technique was used. Let us assume that a person is at a distance D (in centimetres) from camera and the person's actual Width is W (I have assumed that the average width of humans in 41 centimetres). Using the object detection code above, we can identify the pixel height P of the person using the bounding box coordinates. Using these values, the focal length of the camera can be calculated using the below formula:

```
Eq 1 : F = (P x D) / H
```

<br/>
[Explanation Image](png.png)
<br/>

## Then Detect the Distance between the Camera and Object

After calculating the focal length of the camera, we can use the actual Width W of the person, pixel height P of the person and focal length of camera F to calculate the distance of the person from camera.

In my system the Focal Length is :  `790`

But, Here we might not the data of each person's height so, we assume that the average width as  W = 41cm 

```
Eq 2 : D' = (W x F) / P
```

Now that we know the depth of the person from camera, we can move on to calculate the distance between two people in a video. There can be n number of people detected in a video. So the Euclidean distance is calculated between the midpoint of the bounding boxes of all the people detected. By doing this, we have got our x and y values. These pixel values are converted into centimetres using Eq 2.

We have the x, y and z (distance of the person from camera) coordinates for every person in cms. The Euclidean distance between every person detected is calculated using the (x, y, z) coordinates. If the distance between two people is less than 2 metres or 200 centimetres, a red bounding box is displayed around them indicating that they are not maintaining social distance. The object's distance from camera was converted to feet for visualization purpose.

<br/><br/>

# For Better Accurate Results 
* Video can be calibrated to get bird's eye view for more accurate distance estimation between objects.

<br/><br/>

# Setup 
```
pip install -r requirements.txt
```

<br/><br/>

# To Execute Run..
```
python social_distance_detection.py --prototxt SSD_MobileNet_prototxt.txt --model SSD_MobileNet.caffemodel --labels class_labels.txt
```

<br/><br/>

# References
[Social-Distance-Detection-using-OpenCV by Subikshaa](https://github.com/Subikshaa/Social-Distance-Detection-using-OpenCV) Did a few changes and imporvements to this code for better results..

Thanks to [Subikshaa](https://github.com/Subikshaa)..
