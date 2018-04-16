###################################################################################
# Project           : HQ Trivia Aid
# Author            : Jeffrey Lu
# Date created      : 20180412
# Purpose           : Optical character recognition (OCR)
# Revision History  :
# Date          Author      Rev    Changelog
# 20180412    Jeffrey Lu     1     Initial
###################################################################################
import pytesseract
import PIL.Image

class ocr:
    def __init__(self, image_name, image_extension = '.png', debug = 0):
        self.image_name         = image_name                                                # Image file name
        self.image_extension    = image_extension                                           # image extension format
        self.debug              = debug                                                     # Print debug info

    def image2text(self):
        self.image              = PIL.Image.open(self.image_name + self.image_extension)    # Open image in directory
        self.text               = pytesseract.image_to_string(self.image)                   # Convert image to text

        # Debug mode
        if(self.debug == 1):
            self.image.show                                                                 # Display image to be converted
            print(self.text)                                                                # Display text after conversion

        return self.text