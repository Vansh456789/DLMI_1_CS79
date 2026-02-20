import cv2
import numpy as np
import os
from skimage.filters import threshold_niblack, threshold_sauvola

# METRICS

def dice_score(y_true, y_pred):
    intersection = np.sum(y_true & y_pred)
    return (2.0 * intersection) / (np.sum(y_true) + np.sum(y_pred) + 1e-8)

def sensitivity_score(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    return TP / (TP + FN + 1e-8)

# PATH 

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "DRIVE"))
images_folder = os.path.join(base_path, "training", "images")
mask_folder   = os.path.join(base_path, "training", "mask")
gt_folder     = os.path.join(base_path, "training", "1st_manual")

# PROCESS DATASET

dice_niblack_all = []
dice_sauvola_all = []
sens_niblack_all = []
sens_sauvola_all = []

print("Processing DRIVE dataset...\n")

for img_file in sorted(os.listdir(images_folder)):

    if not img_file.endswith(".tif"):
        continue

    image_id = img_file.split("_")[0]

    image_path = os.path.join(images_folder, img_file)
    mask_path  = os.path.join(mask_folder, f"{image_id}_training_mask.gif")
    gt_path    = os.path.join(gt_folder, f"{image_id}_manual1.gif")

    if not (os.path.exists(mask_path) and os.path.exists(gt_path)):
        continue

    # Load image
    img = cv2.imread(image_path)
    green = img[:, :, 1]   # Green channel best for vessels

    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    gt   = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)

    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    _, gt = cv2.threshold(gt, 127, 255, cv2.THRESH_BINARY)

    mask_bin = mask > 0
    gt_bin = gt > 0

    # SEGMENTATION

    niblack_thresh = threshold_niblack(green, window_size=25, k=0.2)
    niblack_binary = (green < niblack_thresh) & mask_bin

    sauvola_thresh = threshold_sauvola(green, window_size=25, k=0.2)
    sauvola_binary = (green < sauvola_thresh) & mask_bin

    # METRICS 

    gt_fov = gt_bin[mask_bin]
    niblack_fov = niblack_binary[mask_bin]
    sauvola_fov = sauvola_binary[mask_bin]

    dice_niblack_all.append(dice_score(gt_fov, niblack_fov))
    dice_sauvola_all.append(dice_score(gt_fov, sauvola_fov))

    sens_niblack_all.append(sensitivity_score(gt_fov, niblack_fov))
    sens_sauvola_all.append(sensitivity_score(gt_fov, sauvola_fov))

# FINAL RESULTS

print("===== FINAL RESULTS =====\n")

print("NIBLACK:")
print("Average Dice       :", np.mean(dice_niblack_all))
print("Average Sensitivity:", np.mean(sens_niblack_all))

print("\nSAUVOLA:")
print("Average Dice       :", np.mean(dice_sauvola_all))
print("Average Sensitivity:", np.mean(sens_sauvola_all))