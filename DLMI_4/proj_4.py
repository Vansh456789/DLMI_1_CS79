import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from skimage import filters, morphology
import os

# ONFIGURATION 
base_path = "data-science-bowl-2018"
train_path = os.path.join(base_path, "stage1_train")

if not os.path.exists(train_path):
    raise FileNotFoundError(
        "Dataset folder not found. "
        "Make sure 'data-science-bowl-2018/stage1_train' exists."
    )

sample_ids = os.listdir(train_path)
sample_id = sample_ids[0]

image_path = os.path.join(train_path, sample_id,
                          "images", sample_id + ".png")

if not os.path.exists(image_path):
    raise FileNotFoundError("Image not found. Check dataset structure.")

print("Processing Sample:", sample_id)

# LOAD IMAGE 
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# PREPROCESSING 
blur = cv2.GaussianBlur(gray, (5, 5), 0)

threshold_value = filters.threshold_otsu(blur)
binary = blur > threshold_value

binary = morphology.remove_small_objects(binary, min_size=50)
binary = ndi.binary_fill_holes(binary)

# DISTANCE TRANSFORM
distance = ndi.distance_transform_edt(binary)

# MARKER DETECTION
coordinates = peak_local_max(distance,
                             min_distance=20,
                             labels=binary)

markers = np.zeros_like(distance, dtype=int)

for i, coord in enumerate(coordinates):
    markers[coord[0], coord[1]] = i + 1

markers = ndi.label(markers)[0]

# WATERSHED
labels_with_markers = watershed(-distance, markers, mask=binary)
labels_without_markers = watershed(-distance, mask=binary)

# REGION COUNT
count_with = len(np.unique(labels_with_markers)) - 1
count_without = len(np.unique(labels_without_markers)) - 1

print("Regions without markers:", count_without)
print("Regions with markers:", count_with)

# VISUALIZATION 
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(binary, cmap='gray')
axes[0].set_title("Binary Mask")

axes[1].imshow(labels_without_markers, cmap='nipy_spectral')
axes[1].set_title(f"Without Markers ({count_without})")

axes[2].imshow(labels_with_markers, cmap='nipy_spectral')
axes[2].set_title(f"With Markers ({count_with})")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()