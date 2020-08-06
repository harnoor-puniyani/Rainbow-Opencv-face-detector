# face-detector-opencv-rainbow

This face detector is based on the haarcascades algorithm to detect faces with a cool color changing box resembling rainbow. This program focuses on the frontal face detectionn only.If you want you can go with other types of detections as well. The algorithm is generally used because its quite fast and not that accurate but till some extent , like we cannot build face lock type of thing with this type of algorithms as it is only the color based algorithm , it takes in the image and turns it into greyscale that is black and white and then ry to match the color pattern for the faces , it kinds of loop through it to the whole photo and frame , and returns  true when a face is found.

## usage
---
###### installing requiremnets
```python
python -m pip install -r requirements.txt
```

* To test it on the photo you might have to clone the repository and change the argument of katrina_face.jpg to the name of the photo you are going to pass to it!
And Simply run:
```python
python photo\ detector.py
```

* To test it on the video just simply change to the video name in your directory to the  funny_video.mp4 or vice-versa.Rainbow effect works perfectly on the multiple frames as a single photo is processed only once but videos have multiple frames so it works fine there too.
simply run:
```python
python video_face_detector.py
```
* Now the actual feel comes to the play, Here we need the webcam rainbow it just works perfectly fine.
simply run : 
```python
python  webcam-rainbow.py
```

#### note
you might use `python3` instead of `python` if it doesn't works for you , or you have installed multiple python versiohns.
