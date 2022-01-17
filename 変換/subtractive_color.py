# -*- coding: utf-8 -*

import cv2
import numpy as np

def subtractive_color(img, K=3):
    try:

        if img is None:
            print ('ファイルを読み込めません。')
            import sys
            sys.exit()

        # 次元数を1落とす
        Z = img.reshape((-1, 3))

        # float32型に変換
        Z = np.float32(Z)

        # 基準の定義
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        # K-means法で減色
        ret, label, center = cv2.kmeans(
            Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # UINT8に変換
        center = np.uint8(center)

        res = center[label.flatten()]

        # 配列の次元数と入力画像と同じに戻す
        dst = res.reshape((img.shape))

        # 出力
        cv2.imwrite('./sub_color_' + str(K) + '.jpg', dst)

    except:
        import sys
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        import traceback
        print(traceback.format_tb(sys.exc_info()[2]))


img = cv2.imread('./Lenna.jpg')
# 2～4色
for i in range(2, 5):
    subtractive_color(img, i)