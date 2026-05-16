# Week 5: YOLOv8 Custom Object Detection

This folder contains the complete pipeline for a custom vehicle detection system, developed as part of the IIITH Internship.

## 🛠️ Implementation Details

### 1. Data Preparation (05WT1 & 05WT2)
- **Dataset:** 140 images manually annotated for the class **'Car'**.
- **Preprocessing:** Used `FFmpeg` to scale all images to a width of **384px** (`384:-1`). This ensured the model received uniform input while maintaining the integrity of the normalized bounding box coordinates.

### 2. Training & Overfitting Analysis (05WT3)
- **Model:** YOLOv8n (Nano).
- **Configuration:** Trained for 20 epochs with a batch size of 16.
- **Overfitting Point:** Identified at **Epoch 13**. 
  - *Analysis:* At this stage, the `val/box_loss` reached a minimum of **1.062** before beginning an upward trend (1.072 in Epoch 14), signaling that the model was starting to overfit the training data.

### 3. Performance Metrics
- **mAP50:** 0.869
- **Precision (P):** 0.935
- **Recall (R):** 0.753

### 4. Inference & Media Fusion (05WT4 & 05WT5)
- **Inference:** Ran the trained `best.pt` weights on unseen test images.
- **Final Visualization:** Created a 10-second detection video by looping frames and fusing them with audio using `FFmpeg`.

## 📁 Key Files
- `best.pt`: The optimized model weights from training.
- `train_model.py`: Training script logic.
- `detect_test.py`: Inference script for testing.
- `week5_final_submission.mp4`: The final 10-second processed output video.