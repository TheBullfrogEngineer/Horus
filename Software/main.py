import ctypes

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

ctypes.windll.shcore.SetProcessDpiAwareness(1)
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

cam = cv2.VideoCapture(1)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    img_final = cv2.resize(img_final, (width//2, height//2))
    _, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    #inverted_frame = cv2.flip(frame, 1)
    fr_height, fr_width, _ = img_final.shape
    cam_height, cam_width, _ = frame.shape
    x = (cam_width - fr_width) // 2
    y = (cam_height - fr_height) // 2
    frame[y:y+fr_height, x:x+fr_width, :] = img_final
    cv2.imshow('Screen Capture', frame)
    cv2.waitKey(10)
