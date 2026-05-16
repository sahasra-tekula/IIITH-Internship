import cv2
import os

video_path = "input.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # save every 5th frame (IMPORTANT)
    if count % 5 == 0:
        cv2.imwrite(f"{output_folder}/frame_{saved}.jpg", frame)
        saved += 1

    count += 1

cap.release()
print("Frames extracted!")