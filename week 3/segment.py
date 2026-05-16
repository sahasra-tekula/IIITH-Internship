from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.predict(
    source="frames",
    save=True,
    conf=0.25
)