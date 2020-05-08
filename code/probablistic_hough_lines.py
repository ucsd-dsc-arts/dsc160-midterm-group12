import scipy.misc
from skimage import data, io
from skimage.color import rgb2hsv
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage
import skimage
import cv2

def calc_edges(img_fp):
    """
    Calculating Probablistic Hough Lines 
    
    return nested array of line patterns
    """
    image = io.imread(img_fp)

    # Getting width and height of image
    height, width, _ = image.shape
    
    # Converting image to HSV
    hsv_img = rgb2hsv(image)
    
    # Slicing out different channels
    hue_img = hsv_img[:, :, 0]
    saturation_img = hsv_img[:, :, 1]
    value_img = hsv_img[:, :, 2]
    
    #calculate edges
    sobel_x = ndimage.sobel(value_img, axis=0, mode='constant')
    sobel_y = ndimage.sobel(value_img, axis=1, mode='constant')
    edge_image = np.hypot(sobel_x, sobel_y)
    
    #hough lines
    temp = exposure.rescale_intensity(edge_image,out_range=(-1.0, 1.0))
    edges = skimage.img_as_ubyte(np.clip(temp, -1, 1))
    
    #probablistic Hough Transformation
    #could change if needed need to ask how to choose
    minLineLength = 400
    maxLineGap = 10
    
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    result = image.copy()
    for x in range(0, len(lines)):    
        for x1,y1,x2,y2 in lines[x]:
            cv2.line(result,(x1,y1),(x2,y2),(0,255,255),5)
    return result[:,:,::]
    
