import cv2
import os

folder = "runs/segment/predict"
video_name = "output.mp4"

images = sorted([img for img in os.listdir(folder) if img.endswith(".jpg")])

# read first image
frame = cv2.imread(os.path.join(folder, images[0]))
h, w, _ = frame.shape

# create video
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 5, (w, h))

for image in images:
    path = os.path.join(folder, image)
    frame = cv2.imread(path)
    video.write(frame)

video.release()

print("Video created successfully!")