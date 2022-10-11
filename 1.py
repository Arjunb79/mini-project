# from PIL import Image
# import pytesseract
# import cv2
# img=cv2.imread('test.png')
# tex=pytesseract.image_to_string(Image.open("test.png"),lang="vie")
# print(pytesseract.image_to_string(Image.open("test.png"),lang="vie"))
# cv2.namedWindow("Input image")
# cv2.imshow("input image",img)
# cv2.waitKey(0)
# cv2.destroyWindow("test")
# cv2.destroyWindow("main")



import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('test.png'), lang='vie'))

z = pytesseract.image_to_string(Image.open('test.png'), lang='vie') #njan onnu variable kettiyittu file aakan nokkiyath koche.ithuvare working aanu

#print("മലയാളത്തിൽ")