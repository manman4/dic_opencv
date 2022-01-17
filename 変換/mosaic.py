# -*- coding: utf-8 -*

import cv2

def mosaic(img, alpha=0.1):
    try:

        if img is None:
            print ('ファイルを読み込めません。')
            import sys
            sys.exit()
        
        # 画像の高さと幅
        w = img.shape[1]
        h = img.shape[0]

        # 最近傍法で縮小→拡大することでモザイク加工
        dst = cv2.resize(img, (int(w*alpha), int(h*alpha)))
        dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

        # 出力
        cv2.imwrite('./mosaic_' + str(alpha) + '.jpg', dst)

    except:
        import sys
        print("Error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
        import traceback
        print(traceback.format_tb(sys.exc_info()[2]))


img = cv2.imread('./Lenna.jpg')
mosaic(img)
mosaic(img, 0.2)