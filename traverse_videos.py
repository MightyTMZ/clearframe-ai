import os
import cv2

video_dir = "./data/videos"

interval = 0.5

videos = os.listdir(video_dir)

count = 1

for video in videos:
    os.rename(f"{video_dir}/{video}", f"{video_dir}/video_{count}.mp4")
    count += 1
    

    # cap = cv2.VideoCapture(video)
    # if not cap.isOpened():
    #     print("Failed to open {video}")
    
    # fp