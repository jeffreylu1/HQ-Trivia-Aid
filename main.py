###################################################################################
# Project           : HQ Trivia Aid
# Author            : Jeffrey Lu
# Date created      : 20180412
# Purpose           : Provide the best answer via google search using OCR'ed question
# Revision History  :
# Date          Author      Rev    Changelog
# 20180412    Jeffrey Lu     1     Initial
###################################################################################

import snipping_tool
import ocr
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import time
import googler
import string
import re

# Program parameters
image_name          = 'capture' # File name for captured image
image_extension     = '.png'    # Supports PNG, JPG
debug_mode          = 0         # 1: ON  0: OFF
debug_post_proccess = 0         # 1: ON  0: OFF
debug_timer         = 1         # 1: ON  0: OFF
debug_image_used    = 0
countA = 0
countB = 0
countC = 0

# Instantiate objects
searcher = googler.google()


#Acquire trivia question image
if(debug_image_used == 0):
    app             = QtWidgets.QApplication(sys.argv)
    snip_window     = snipping_tool.snipping_tool(image_name, image_extension)
    snip_window.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.exec_()

if(debug_timer):
    start_time = time.time()

# Convert image to text
while(1):
    try:
        ocr     = ocr.ocr(image_name, image_extension, debug = debug_mode)
        raw_text    = ocr.image2text()
        break
    except:
        print("Try again... Invalid snip")
        app             = QtWidgets.QApplication(sys.argv)
        snip_window     = snipping_tool.snipping_tool(image_name, image_extension)
        snip_window.show()
        app.aboutToQuit.connect(app.deleteLater)
        app.exec_()
        ocr     = ocr.ocr(image_name, image_extension, debug = debug_mode)
        raw_text    = ocr.image2text()

raw_text = raw_text.split('\n')
if(debug_post_proccess):
    print("Raw text: ", raw_text)

# Parse text
while '' in raw_text:
    raw_text.remove('')

question = ' '.join(raw_text[:-3])
C_raw = raw_text.pop()
B_raw = raw_text.pop()
A_raw = raw_text.pop()

# Scrape Google
results = searcher.search_google(question)

# Remove single letter words
C = re.sub(r'\b\w{1,1}\b', '', C_raw)
B = re.sub(r'\b\w{1,1}\b', '', B_raw)
A = re.sub(r'\b\w{1,1}\b', '', A_raw)

# Remove punctuation
new_A = A.split()
new_A = re.findall(r"[\w']+|[.,!?;]", A)

new_B = B.split()
new_B = re.findall(r"[\w']+|[.,!?;]", B)

new_C = C.split()
new_C = re.findall(r"[\w']+|[.,!?;]", C)

# Parse question
for i, desc in enumerate(d['description'] for d in results):
    for worda in new_A:
        try:
            if worda in desc: 
                countA = countA + 1
        except:
            pass
    for wordb in new_B:
        try:
            if wordb in desc:
                countB = countB + 1
        except:
            pass
    for wordc in new_C:
        try:
            if wordc in desc:
                countC = countC + 1
        except:
            pass

total = countA + countB + countC
if(total == 0):
    total = 99999999999999999999

print("Question: ", question)
print("Option A: ", A_raw, " ", countA/total*100)
print("Option B: ", B_raw, " ", countB/total*100)
print("Option C: ", C_raw, " ", countC/total*100)

if(debug_timer):
    elapsed_time = time.time() - start_time
    print("Time elapsed: " + str(elapsed_time))
