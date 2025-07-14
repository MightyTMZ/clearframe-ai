import os
import cv2


to_be_rotated = [
    # "video_2", 
    # "video_6", 
    # "video_7", 
    # "video_8", 
    # "video_9", 
    # "video_10", 
    "video_11", 
    "video_12", 
]

for folder in to_be_rotated:
    print(f"Rotating '{folder}' ")

    image_dir = f"./data/images/{folder}"

    images = os.listdir(image_dir)

    output_dir = f"./data/images/rotated_images_for_{folder}"

    os.makedirs(output_dir, exist_ok=True)

    for image in images:
        image_path = os.path.join(image_dir, image)
        img = cv2.imread(image_path)
        if img is None:
            print(f"Skipping {image_path}, not a valid image.")
            continue
        rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        output_path = os.path.join(output_dir, image)
        cv2.imwrite(output_path, rotated_image)
