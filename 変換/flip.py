# -*- coding: utf-8 -*

import cv2

def flip(img):
    try:

        if img is None:
            print ('ファイルを読み込めません。')
            import sys
            sys.exit()

        # 上下逆
        dst = cv2.flip(img, 0)
        cv2.imwrite('./flip0.jpg', dst)
        cv2.imshow('dst1', dst)

        # 左右反転
        dst = cv2.flip(img, 1)
        cv2.imwrite('./flip1.jpg', dst)
        cv2.imshow('dst2', dst)

        # 上下左右
        dst = cv2.flip(img, -1)
        cv2.imwrite('./flip-1.jpg', dst)
        cv2.imshow('dst3', dst)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    except:
        import sys
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        import traceback
        print(traceback.format_tb(sys.exc_info()[2]))


img = cv2.imread('./Lenna.jpg')
flip(img)