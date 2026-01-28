import os

LABELS_DIR = "datasets/dataset_01/labels"

for split in ["train", "val", "test"]:
    dir_path = os.path.join(LABELS_DIR, split)
    if not os.path.exists(dir_path):
        continue

    for file in os.listdir(dir_path):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(dir_path, file)

        with open(path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            parts[0] = "0"  # corregir clase
            new_lines.append(" ".join(parts) + "\n")

        with open(path, "w") as f:
            f.writelines(new_lines)

print("✅ Clases corregidas a 0")
