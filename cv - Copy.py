{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "source": [
    "from tkinter import *\r\n",
    "import pyautogui\r\n",
    "import cv2\r\n",
    "import numpy as np\r\n",
    "from PIL import Image\r\n",
    "import pytesseract\r\n",
    "import subprocess\r\n",
    "import requests\r\n",
    "import urllib.parse\r\n",
    "import time\r\n",
    "\r\n",
    "time.sleep(4)\r\n",
    "\r\n",
    "\r\n",
    "def getTranslation(text):\r\n",
    " txt = text.replace(\"\\n\",\"\")\r\n",
    " URL =\"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=bn&dt=t&q=\"+urllib.parse.quote(txt);\r\n",
    " r = requests.get(url = URL)\r\n",
    " data = r.json()\r\n",
    " showText(data)\r\n",
    " return data;\r\n",
    "\r\n",
    "def showText(text):\r\n",
    " root = Tk()\r\n",
    " AdviseBox = Text(root, width=50, height=20)\r\n",
    " AdviseBox.pack(side=RIGHT, expand=YES, padx=5, pady=5)\r\n",
    " AdviseBox.insert(INSERT, text)\r\n",
    " root.mainloop()\r\n",
    "def openNotepad(text):\r\n",
    " subprocess.Popen([\"notepad\",\"filename.txt\"])\r\n",
    "def getText(c_image):\r\n",
    " im = Image.open(\"s/screen.png\")\r\n",
    " pytesseract.pytesseract.tesseract_cmd = r'D:/PortableApps/ocrlib/tesseract.exe'\r\n",
    " text = pytesseract.image_to_string(c_image, lang = 'eng')\r\n",
    " return text\r\n",
    "\r\n",
    "def getScreenShot():\r\n",
    " screenshot = pyautogui.screenshot()\r\n",
    " screenshot.save(\"s/screen.png\")\r\n",
    "\r\n",
    "getScreenShot();\r\n",
    "image = cv2.imread('s/screen.png')\r\n",
    "oriImage = image.copy()\r\n",
    "cv2.imshow(\"image\", image)\r\n",
    "\r\n",
    "\r\n",
    "\r\n",
    "cropping = False\r\n",
    "x_start, y_start, x_end, y_end = 0, 0, 0, 0\r\n",
    "def mouse_crop(event, x, y, flags, param):\r\n",
    "    # grab references to the global variables\r\n",
    "    global x_start, y_start, x_end, y_end, cropping\r\n",
    "\r\n",
    "    # if the left mouse button was DOWN, start RECORDING\r\n",
    "    # (x, y) coordinates and indicate that cropping is being\r\n",
    "    if event == cv2.EVENT_LBUTTONDOWN:\r\n",
    "        x_start, y_start, x_end, y_end = x, y, x, y\r\n",
    "        cropping = True\r\n",
    "\r\n",
    "    # Mouse is Moving\r\n",
    "    elif event == cv2.EVENT_MOUSEMOVE:\r\n",
    "        if cropping == True:\r\n",
    "            x_end, y_end = x, y\r\n",
    "\r\n",
    "    # if the left mouse button was released\r\n",
    "    elif event == cv2.EVENT_LBUTTONUP:\r\n",
    "        # record the ending (x, y) coordinates\r\n",
    "        x_end, y_end = x, y\r\n",
    "        cropping = False # cropping is finished\r\n",
    "\r\n",
    "        refPoint = [(x_start, y_start), (x_end, y_end)]\r\n",
    "\r\n",
    "        if len(refPoint) == 2: #when two points were found\r\n",
    "            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]\r\n",
    "            #cv2.imshow(\"Cropped\", roi)\r\n",
    "            text = getText(roi)\r\n",
    "            showText(text)\r\n",
    "            getTranslation(text)\r\n",
    "\r\n",
    "\r\n",
    "cv2.namedWindow(\"image\")\r\n",
    "cv2.setMouseCallback(\"image\", mouse_crop)\r\n",
    "\r\n",
    "\r\n",
    "while True:\r\n",
    "    i = image.copy()\r\n",
    "    k = cv2.waitKey(200)\r\n",
    "    if not cropping:\r\n",
    "        cv2.imshow(\"image\", image)\r\n",
    "\r\n",
    "    elif cropping:\r\n",
    "        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)\r\n",
    "        cv2.imshow(\"image\", i)\r\n",
    "    if k in [27, 1048603]: # ESC key to abort, close window\r\n",
    "        cv2.destroyAllWindows()\r\n",
    "        break\r\n",
    "    \r\n",
    "\r\n"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [],
   "outputs": [],
   "metadata": {}
  }
 ],
 "metadata": {
  "orig_nbformat": 4,
  "language_info": {
   "name": "python",
   "version": "3.10.3",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.10.3 64-bit"
  },
  "interpreter": {
   "hash": "344d67a82e873fd2857d0b64807739f0aa462da8c99071cb38d9649b961a3c37"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}