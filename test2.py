# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:10:25 2019

@author: Azumi Mamiya
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

# 画像を読み込む。
img = cv2.imread('image/40_XY01_00001_CH1.tif')

# 画像を表示する。
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img)
ax.axis('off')
plt.show()