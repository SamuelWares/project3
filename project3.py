# CPS121 Project 3
# Written: <11/21/2024> <Samuel Wares> <samuel.wares@gordon.edu>
# 
# <Include description of program here>
##
# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   Y Altering colors of the image
#   Y Grayscale
#   Y Making darker or lighter
#   Y Sepia-toned
#   _ Posterized
#   Need nested loops
#   Y Mirrorizing
#   _ Edge detection
#   _ Chromakey (change background)
#   Y Blurring
#   Need nested loops and alter size or shape
#   Y Rotation
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
def makeDaytime(picture):
    """Supporting function: makes a sunset turn into daytime"""
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            picture.setRed(x,y, picture.getRed(x,y)*0.5)
            
def xmirror(picture):
    """Supporting function: Mirrors image across the x-axis"""
    for x in range(0,picture.getWidth()):
        for y in range(0,picture.getHeight()//2):
            color = picture.getColor(x,y)
            picture.setColor(x,y,color)
            picture.setColor(x,picture.getHeight()-y,color)

def ymirror(picture):
    """Supporting function: Mirrors an image across the y-axis"""            
    for x in range(0,picture.getWidth()//2):
        for y in range(0,picture.getHeight()):
            color = picture.getColor(x,y)
            picture.setColor(x,y,color)
            picture.setColor(picture.getWidth()-x,y,color)

def grayScale(picture):
    """Supporting function: Makes an image gray"""
    for x in range(0,picture.getWidth()):
        for y in range(0,picture.getHeight()):
            p = (x,y)
            value = (picture.getRed(p[0],p[1]) + picture.getGreen(p[0],p[1])
            +picture.getBlue(p[0],p[1]))//3
            picture.setRed(p[0],p[1],value)
            picture.setGreen(p[0],p[1],value)
            picture.setBlue(p[0],p[1],value)

def sepiaTint(picture):
    """Supporting function: Make a picture look old, supported by grayScale(x)"""
    grayScale(picture)
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            red = picture.getRed(x,y)
            blue = picture.getBlue(x,y)
            #tint shadows
            if (red < 63):
                red = red*1.1
                blue = 0.9*blue
            #tint midtones
            if (red > 62 and red < 192):
                red = red*1.15
                blue = blue*0.85
            #tint highlghts
            if (red >191):
                red = red*1.08
            if (red > 255):
                red = 255
                blue = blue*0.93
            #set the new color values
            picture.setBlue(x,y, blue)
            picture.setRed(x,y,red)

def rotate(picture):
    """Supporting function: rotates a picture clockwise"""
    canvas = pgt.Picture(picture.getHeight(), picture.getWidth())
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            color = picture.getColor(x,y)
            canvas.setColor(picture.getHeight()-y,x,color)
    return canvas

def blurring(picture):
    """Supporting function: blurrs a picture"""
    canvas = pgt.Picture(picture.getHeight(), picture.getWidth())
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            if (x%4 == 0 and y%4 == 0) and (picture.getPixel(x+4,y+4) is not None):
                color = picture.getColor(x,y)
                for i in range(0,4):
                    for j in range(0,4):  
                        picture.setColor(x+i,y+j,color)
                    

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
    pic1 = pgt.Picture('picture1.jpg')
    pic2 = pgt.Picture('picture2.jpg')
    pic3 = pgt.Picture('picture3.jpg')
    pic4 = pgt.Picture('picture4.jpg')
    pic5 = pgt.Picture('picture5.jpg')
    widthpic2 = pic2.getWidth()
    heightpic3 = pic3.getHeight()
    widthpic4 = pic4.getWidth()
    heightpic4 = pic4.getHeight()
    widthpic5 = pic5.getWidth()
    heightpic5 = pic5.getHeight()
    ymirror(pic1)
    xmirror(pic2)
    grayScale(pic1)
    sepiaTint(pic2)
    blurring(pic4)
    pic1 = rotate(pic1)
    pic1 = rotate(pic1)
    makeDaytime(pic3)
    pic1.copyInto(collage, 0, 0)
    pic2.copyInto(collage, 700-widthpic2, 0)
    pic3.copyInto(collage, 0, 950-heightpic3)
    pic4.copyInto(collage, 700-widthpic4, 950-heightpic4)
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
    text = "<!DOCTYPE html>\n"
    text += "<title>Samuel's Collage</title>\n"
    text += "<h1>Samuel's Collage</h1>\n"
    text += f'<img src="{imageFile}" alt="Samuels Collage>\n'
    htmlFile.write(text)
    print("output file:", htmlFile.name)
    htmlFile.close()    







# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = "collage.jpg"
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