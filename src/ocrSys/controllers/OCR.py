from PIL import Image
from pyocr import tesseract

class OCR():
    def scanImage(self, img):
        if(tesseract.is_available()):
            return tesseract.image_to_string(Image.open(img))
        else:
            return "FAIL"