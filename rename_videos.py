import os

video_dir = "./data/videos"
videos = os.listdir(video_dir)
count = 1

for video in videos:
    os.rename(f"{video_dir}/{video}", f"{video_dir}/video_{count}.mp4")
    count += 1