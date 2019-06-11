# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 00:20:08 2019

@author: Azumi Mamiya
"""

# -*- coding: utf-8 -*-
 
import cv2
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle
import matplotlib.pyplot as plt


def draw_contours(ax, img, contours):
    ax.imshow(img)
    ax.axis('off')
    for i, cnt in enumerate(contours):
        cnt = np.squeeze(cnt, axis=1)  # (NumPoints, 1, 2) -> (NumPoints, 2)
        # 輪郭の点同士を結ぶ線を描画する。
        ax.add_patch(Polygon(cnt, color='b', fill=None, lw=1))
        # 輪郭の点を描画する。
        ax.plot(cnt[:, 0], cnt[:, 1], 'ko', mew=0, ms=4)
        # 輪郭の番号を描画する。
        ax.text(cnt[0][0], cnt[0][1], i, color='red', size='8')
    print(i)

def contArea():
    
    for i, cnt in enumerate(contours):
        # 輪郭の面積を計算する。
        area = cv2.contourArea(cnt)
        print('contour: {}, area: {}'.format(i, area*2.2))

if __name__ == '__main__':
 
    # 画像の読み込み
    img_src = cv2.imread("image/40_XY01_00002_CH1.tif", 1)
 
    # グレースケールに変換
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
 
    # 二値変換
    thresh = 29#閾値27
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_gray,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)
    img_dst=cv2.bitwise_not(img_dst)#白黒反転
    contours, hierarchy = cv2.findContours(img_dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #img_dst = cv2.drawContours(img_dst, contours, -1, (0,255,0), 3)
    # 表示
    contArea()
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    draw_contours(ax, img_dst, contours)
    plt.show()
    
    img_dst = cv2.drawContours(img_dst, contours, -1, (0,255,0), 1)
    cv2.imshow("Show BINARIZATION Image", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()