import cv2
import os

# path = './data/images/video_4/video_4_snapshot_0000.jpg'

# image = cv2.imread(path)
# print(type(image))

# rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imshow("90° Clockwise", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

foldername = "video_5"

image_dir = f"./data/images/{foldername}"

images = os.listdir(image_dir)

output_dir = f"./data/images/rotated_images_for_{foldername}"

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

