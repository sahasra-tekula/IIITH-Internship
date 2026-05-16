import os
import shutil

frames_dir = "frames"
train_dir = "dataset/images/train"
val_dir = "dataset/images/val"
test_dir = "dataset/images/test"

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

frames = sorted(os.listdir(frames_dir))
total = len(frames)

train_count = 100
val_count = 40

# pick evenly spaced indices
indices = list(range(0, total, total // (train_count + val_count)))

selected = [frames[i] for i in indices[:train_count + val_count]]

train_frames = selected[:train_count]
val_frames = selected[train_count:train_count + val_count]

# rest → test
test_frames = [f for f in frames if f not in train_frames + val_frames]

# copy files
for f in train_frames:
    shutil.copy(os.path.join(frames_dir, f), os.path.join(train_dir, f))

for f in val_frames:
    shutil.copy(os.path.join(frames_dir, f), os.path.join(val_dir, f))

for f in test_frames:
    shutil.copy(os.path.join(frames_dir, f), os.path.join(test_dir, f))

print(f"Train: {len(train_frames)}, Val: {len(val_frames)}, Test: {len(test_frames)}")