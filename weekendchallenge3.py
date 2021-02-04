#import required libraries
from PIL import Image
import cv2
import random
import numpy as np


#load image to be used
orig_img= cv2.imread('/home/kate/moon.png')

def invert_image(orig_img):
    #grayscale the image 
    gray_image= cv2.cvtColor(orig_img,cv2.COLOR_BGR2GRAY)
    #invert the image
    inv_img = cv2.bitwise_not(gray_image)
    cv2.imshow('invert', inv_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#sepia toning the image
def sepia_tone(orig_img):
    #grayscale the image
    #gray_image= cv2.cvtColor(orig_img,cv2.COLOR_BGR2GRAY)
   # cv.imshow('gray',gray_image)


    img = orig_img
    original = img.copy()
    img = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix implementing the bgr thingy
    img[np.where(img > 255)] = 255 # normalizing values greater than 255 to 255
    img = np.array(img, dtype=np.uint8) # converting back to int
    cv2.imshow("original", original)
    cv2.imshow("Output", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gray_image(orig_img):
    gray_img = cv2.cvtColor(orig_img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def black_and_white(orig_img):
    #read image wile in grayscale
    img_grey =  cv2.cvtColor(orig_img,cv2.COLOR_BGR2GRAY)


    # define a threshold, 128 is the middle of black and white in grey scale
    thresh = 128

    # threshold the image
    img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

    #show the image


    cv2.imshow('output',img_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def main():
    #load image
    orig_img= cv2.imread('/home/kate/moon.png')
    cv2.imshow('original',orig_img)
    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #run the random thingy to know which filter to use
    filt = random.randint(1,4)
    print(filt)


    if filt ==1:
        print("INVERT")
        invert_image(orig_img)

    elif filt ==2:
        print("SEPIA TONE")
        sepia_tone(orig_img)

    elif filt ==3:
        print("Gray")
        gray_image(orig_img)
        
    elif filt ==4:
        print("black and white")
        black_and_white(orig_img)

if __name__=='__main__':
        main()

