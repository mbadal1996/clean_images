# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:32:00 2021

@author: mbadal1996
"""

#!/usr/bin/env python
# coding: utf-8

# ======================================================================
# clean_images v1.0
# Comments:
#    
# The following code removes images from a folder as part of the cleaning 
# process necessary in many machine learning tasks. The list of images called 
# 'img_clean_list' has to be manually created by the user as a list. 
# While this is labor intensive and not an automatic solution, it only has
# to be done once.
#
# The code will accurately delete the images whose name is provided in the 
# list (e.g 0,1,2,3,...), and if one or more images is not found, the code 
# will give a warning message, provide the name of the missing image(s), 
# and continue deleting the remaining ones. The code assumes that the 
# images have a .jpg extension but this can be easily modified.
#
# The code runs fast enough so that even thousands of images require 
# only 1-2 seconds for deletion. 
#
# ======================================================================

# Python 
import os


# Example list of images to delete
img_clean_list = [0,2,3,5,12]


# Example files location for images (Windows example)
location = "C:/Documents/Math/Research/pics"


# Loop through and delete images in image folder 
for i in range(len(img_clean_list)):
    file = str(img_clean_list[i])+".jpg"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    else:
        print(path)
        pass

