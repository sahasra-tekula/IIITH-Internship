from ultralytics import YOLO
import os

# 1. Load your newly learned weights 
# Note: Using the exact path from your last successful training run
model = YOLO('runs/detect/train-3/weights/best.pt')

# 2. Update the source path to match your folder
# We use the full path to be 100% sure it finds it
source_path = 'D:/IIITH-Internship/week 5/dataset/valid/images'

# 3. Run detection
results = model.predict(
    source=source_path, 
    save=True, 
    conf=0.25  # Lowered to 0.25 to see more potential detections
)

print(f"Detections complete. Check the 'runs/detect/predict' folder.")