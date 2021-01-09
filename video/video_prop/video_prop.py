# -*- coding: utf-8 -*

import cv2

def video_prop(filename):
    # 動画の読み込み
    video = cv2.VideoCapture(filename)

    # 幅
    W = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    # 高さ
    H = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # 総フレーム数
    count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # fps
    fps = video.get(cv2.CAP_PROP_FPS)

    return [W, H, count, fps]

print(video_prop("Girl.mp4"))