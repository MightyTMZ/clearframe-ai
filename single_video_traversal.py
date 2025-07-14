import os
import cv2

video_dir = "./data/videos"
images_dir = "./data/images"

interval = 0.5

videos = os.listdir(video_dir)

video = "video_11.mp4"

output_dir = "new_video_traversal" # os.path.join(images_dir, video[:-4])
os.makedirs(output_dir, exist_ok=True)

print(output_dir)

cap = cv2.VideoCapture(os.path.join(video_dir, video))
if not cap.isOpened():
    print("Failed to open {video}")

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# duration = total_frames / fps
frame_interval = int(fps * interval)

video_name = os.path.splitext(os.path.basename(video))[0]
frame_idx = 0
snapshot_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_idx % frame_interval == 0:
        snapshot_name = f"{video_name}_snapshot_{snapshot_idx:04d}.jpg"
        cv2.imwrite(os.path.join(output_dir, snapshot_name), frame)
        snapshot_idx += 1

    frame_idx += 1

cap.release()
print(f"Finished processing {video}")
