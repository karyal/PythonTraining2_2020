# Import the necessary libraries
import cv2
import os
import sys
try:
    image = cv2.imread("source_image1.png")
    image = cv2.imread("source_image4.png")
    cascPath = 'haarcascade_frontalface_default.xml'

    # Make a copy to prevent us from modifying the original
    color_img = image.copy()
    filename = os.path.basename("source_image1.png")

    # OpenCV works best with gray images
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # Use OpenCV's built-in Haar classifier
    # haar_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    haar_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)

    # faces = haar_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
    faces = haar_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    print('Number of faces found: {faces}'.format(faces=len(faces)))

    # Create rectangle on faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Faces on Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("Error : ", sys.exc_info()[1])