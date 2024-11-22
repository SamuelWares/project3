# CPS121 Project 3
# Written: <date> <fullname> <email>
# 
# <Include description of program here>
##
# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   _ Altering colors of the image
#   _ Grayscale
#   _ Making darker or lighter
#   _ Sepia-toned
#   _ Posterized
#   Need nested loops
#   _ Mirrorizing
#   _ Edge detection
#   _ Chromakey (change background)
#   _ Blurring
#   Need nested loops and alter size or shape
#   _ Rotation
#   _ Cropping
#   _ Shifting
#   Other transformations
#   _ <description of transformation>
#   _ <description of transformation>
#   _ <description of transformation>
# ============================================================================

import GCPictureTools as pgt
import pygame as pg
import os, sys
import traceback

# ============================================================================
# ================ Start making changes after this comment ===================
# ============================================================================

# ---- SUPPORTING FUNCTIONS SHOULD GO HERE ----

def createCollage():
    """Create a collage.
 
    Returns
    -------
    Picture
        the collage.
    """
    # create "canvas" on which to make a collage.  You may exchange the
    # width and height values if you prefer a landscape orientation.
    collage = pgt.Picture(700, 950)

    # ---- YOUR CODE TO BUILD THE COLLAGE GOES HERE ----
    # Notice that this is **inside** the createCollage() function.  Because
    # createCollage() should be a "one-and-only-one-thing" function, you
    # should use supporting functions to do transformations, etc.  These
    # supporting functions should be defined below, after the code for this
    # function.
    pic = pgt.Picture('arch.jpg')

    pic.copyInto(collage, 200, 100)
    pic.copyInto(collage, 300, 300)
    pic.copyInto(collage, 100, 300)
    return collage

def createWebPage(imageFile, webPageFile):
    """Create web page that contains the collage.
    Parameter: imageFile - the image file name 
    Parameter: webPageFile - the finename of the output web page 
    Returns
    -------
    nothing
    """

    htmlFile = open(webPageFile, "wt")

    # ---- YOUR CODE TO BUILD THE Webpage with the COLLAGE GOES HERE ----
   

    print("output file:", htmlFile.name)
    htmlFile.close()    







# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = None
    htmlFileName = "webpage.html"  #Default name

    if len(sys.argv) > 1:
        collageFile = sys.argv[1]
    if len(sys.argv) > 2:
        htmlFile = sys.argv[2]    

    # temporarily set media path to project directory
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # create the collage
    
    collage = createCollage()
    #collage.display()

    try:
        # either show collage on screen or write it to file
        if collageFile is None:
            collage.display()
            input('Press Enter to quit...')
        else:
            print(f'Saving collage to {collageFile}')
            collage.save(collageFile)
            createWebPage(collageFile, htmlFileName)
    except:
        print('Could not show or save picture')

