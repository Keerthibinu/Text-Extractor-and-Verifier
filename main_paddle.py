"""
To extract text from image
"""

from paddleocr import PaddleOCR

IMAG = '/home/keerthi/newmini/img4.png'
ocr = PaddleOCR()
result = ocr.ocr(IMAG)

list1 = []
list2 = []
for i in range(len(result[0])):
    str1 = result[0][i][1][0]
    list1 = str1.split(" ")
    list2.extend(list1)
STR2 = " ".join(map(str, list2))
print(STR2)
