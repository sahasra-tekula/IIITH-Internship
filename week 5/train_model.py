from ultralytics import YOLO

# 1. Load the pre-trained nano model
model = YOLO('yolov8n.pt')

# 2. Start training
# We use device='cpu' as per your machine setup
results = model.train(
    data='dataset/data.yaml', 
    epochs=20, 
    imgsz=384, 
    device='cpu'
)