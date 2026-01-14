import os
import cv2
import numpy as np

datasets = {
    "Pneumonie": {
        "raw": r"D:\Facultate\RN\docs\raw\Pneumonie",
        "processed": r"D:\Facultate\RN\docs\processed\Pneumonia"
    },
    "Tuberculoza": {
        "raw": r"D:\Facultate\RN\docs\raw\Tuberculoza",
        "processed": r"D:\Facultate\RN\docs\processed\Tuberculoza"
    }
}

IMG_SIZE = (224, 224)

def remove_hard_white_bands(img):
    """
    Identifică benzile albe pure și le reconstruiește folosind Inpainting.
    """
  
    _, mask = cv2.threshold(img, 252, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    img_cleaned = cv2.inpaint(img, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img_final = clahe.apply(img_cleaned)
    
    return img_final

def preprocess_dataset():
    for name, paths in datasets.items():
        raw_dir = paths["raw"]
        proc_dir = paths["processed"]
        os.makedirs(proc_dir, exist_ok=True)

        files = [f for f in os.listdir(raw_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        print(f"Curățare avansată pentru {name}...")

        count = 0
        for filename in files:
            img_path = os.path.join(raw_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            if img is None: continue

            img_processed = remove_hard_white_bands(img)

            img_resized = cv2.resize(img_processed, IMG_SIZE, interpolation=cv2.INTER_AREA)

            save_path = os.path.join(proc_dir, os.path.splitext(filename)[0] + ".png")
            cv2.imwrite(save_path, img_resized)
            
            count += 1
            if count % 500 == 0: print(f"Progres: {count}...")

        print(f"Gata {name}!\n")

if __name__ == "__main__":
    preprocess_dataset()