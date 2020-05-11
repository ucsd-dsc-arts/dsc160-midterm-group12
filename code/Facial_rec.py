# Importing libraries
from skimage import io
import cv2
import os
import pandas as pd


def facial_detection(img_fp):
    """ 
    Returns the location of a face box, eyes, and smile
    if none is detected () is returned
    """
    image = io.imread(img_fp) 
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        portrait_cv = cv2.rectangle(image_cv,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image_cv[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        portrait_cv = cv2.rectangle(image_cv,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image_cv[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        smiles = smile_cascade.detectMultiScale(roi_gray)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
          
    # Checks the existence of facial features
    if ('eyes' not in locals()) and ('smiles' not in locals()):
        return 0
    else:
        if (len('eyes') > 0) or (len('smiles') > 0):
            return 1
        else:
            return 0
    
    
    
def get_detection(fp):
    """
    Takes in a path to an image directory and
    creates a dataframe on whether a facial feature
    was detected in each image
    """
    
    imgs = os.listdir(fp)
    has_facial = []
    
    # Detecting facial features
    for img in imgs:
        print(img)
        img_fp = fp+img
        detect = facial_detection(img_fp)
        print(detect)
        has_facial.append(detect)
        
    # Saving information
    img_df = pd.DataFrame({'name': imgs, 
                          'facial': has_facial})
    img_df.to_csv('facial.csv', index=False)
    