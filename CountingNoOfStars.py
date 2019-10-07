# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Importing the libraries
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

#Importing the image
example_file = glob.glob(r"wint_sky.gif")[0]
im = imread(example_file)
plt.imshow(im)
#Converting the image to gray scale
plt.gray()
plt.imshow(im)

#Doing all the computation
blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)

#Validating whether we captured all the stars
fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=None)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)