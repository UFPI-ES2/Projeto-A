'''
Created on 21/06/2015

@author: Anderson
'''
from PIL import Image
import pytesseract as tess


class OcrBorder:
    def do_ocr(self, image):
        img = None
        print("do_ocr: " + str(type(image)))
        if(isinstance(image, Image.Image)):
            print("obj")
            img = image
            print("oh: " + str(type(image)))
        else:
            img = Image.open(image)
        print("oh: hear " + str(type(img)))
        ret = tess.image_to_string(img)
        return ret
