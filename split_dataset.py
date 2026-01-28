import os
import random
import shutil

BASE = "datasets/project-2_dataset"
OUT = "datasets/dataset_01"

SPLITS = {
    "train": 0.7,
    "val": 0.2,
    "test": 0.1
}

images_dir = os.path.join(BASE, "images")
labels_dir = os.path.join(BASE, "labels")

images = [f for f in os.listdir(images_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
random.shuffle(images)

start = 0
for split, ratio in SPLITS.items():
    os.makedirs(os.path.join(OUT, "images", split), exist_ok=True)
    os.makedirs(os.path.join(OUT, "labels", split), exist_ok=True)

    end = start + int(len(images) * ratio)

    for img in images[start:end]:
        src_img = os.path.join(images_dir, img)
        dst_img = os.path.join(OUT, "images", split, img)

        label = os.path.splitext(img)[0] + ".txt"
        src_label = os.path.join(labels_dir, label)
        dst_label = os.path.join(OUT, "labels", split, label)

        shutil.copy(src_img, dst_img)

        if os.path.exists(src_label):
            shutil.copy(src_label, dst_label)
        else:
            print(f"⚠ Label no encontrado para {img}")

    start = end

print("✅ Dataset dividido correctamente")
