# HQ Trivia Aid

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
System Requirements

```
Windows
```

Software
```
Python 3.6.4 or later (32-bit)
tesseract for Windows: http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
```

Python Libraries
```
$ pip install -r libraries.txt
or
$ pip install python-qt5
$ pip install pillow
$ pip install numpy
$ pip install opencv-python
$ pip install tesseract
$ pip install search_google
```

Script Setup
```
Go to pytesseract.py
Edit line 42 to point to Windows installation path of tesseract ocr
$ tesseract_cmd = 'c:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
```

## Start
```
$ python main.py
Snip a screenshot of question and answers as shown in test image
```

## License
Licensed under the terms of the MIT License (see the file LICENSE)

## Version
1.0

## Authors
**Jeffrey Lu**