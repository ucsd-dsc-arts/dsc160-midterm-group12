""" Image Feature

features.py calculates a series of statistics/features 
for a specified image.

"""


# Importing libraries
from skimage import io
from skimage.color import rgb2hsv
import skimage
import numpy as np
import os


def calc_stats(img_fp):
    """
    Calculates height, width, mean hue, saturation, 
    value, and the energy of an image.
    
    :param img_fp: Filepath to image
    :returns: List containing image statistics
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
    
    # Calculating averages
    mean_hue = np.mean(hue_img, axis=(0,1))
    mean_saturation = np.mean(saturation_img, axis=(0,1))
    mean_value = np.mean(value_img, axis=(0,1))
    
    # Computing energy of image
    image_arr = np.array(image, dtype=int)
    
    # Calculating squared differences across RGD pixels
    deltaX = np.square(np.roll(image_arr, -1, axis=0) - 
                       np.roll(image_arr, 1, axis=0)
                      )
    deltaY = np.square(np.roll(image_arr, -1, axis=1) - 
                       np.roll(image_arr, 1, axis=1)
                      )

    # Adding RGB values for each pixel, then shifting
    dualEnergy = np.sum(deltaX, axis=2)+np.sum(deltaY, axis=2)
    
    mean_energy = np.mean(dualEnergy)
    
    return [height, width, mean_hue, mean_saturation, 
            mean_value, mean_energy]
