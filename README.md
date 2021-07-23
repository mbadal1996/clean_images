# clean_images
The purpose of the python code clean_images is to remove unwanted images from a folder for NN training

=====================================================================

clean_images v1.0

Comments:
   
The following python code removes images from a folder as part of the cleaning 
process necessary in many machine learning tasks. The list of images called 
'img_clean_list' has to be manually created by the user as a list. 
While this is labor intensive and not an automatic solution, it only has
to be done once.

The code will accurately delete the images whose name is provided in the 
list (e.g 0,1,2,3,...), and if one or more images is not found, the code 
will give a warning message, provide the name of the missing image(s), 
and continue deleting the remaining ones. The code assumes that the 
images have a .jpg extension but this can be easily modified.

The code runs fast enough so that even thousands of images require 
only 1-2 seconds for deletion. 

======================================================================
