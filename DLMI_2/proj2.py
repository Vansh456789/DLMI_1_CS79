import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import skfuzzy as fuzz
from sklearn.metrics import adjusted_rand_score
from skimage import measure

# ==================== CONFIGURATION ====================
image_path = "blood_cell.jpg"   # <-- update to your image
# ========================================================

# Load image and convert to LAB colour space (better for clustering)
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Reshape to pixel vectors
pixels = img_lab.reshape((-1, 3)).astype(np.float32)

# ---------- K‑means clustering ----------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(pixels)
kmeans_seg = kmeans_labels.reshape(img.shape[:2])

# ---------- Fuzzy C‑means clustering ----------
# Data needs to be (features, samples)
data = pixels.T
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data, c=3, m=2, error=0.005, maxiter=1000, init=None
)
fcm_labels = np.argmax(u, axis=0)
fcm_seg = fcm_labels.reshape(img.shape[:2])

# ---------- Compare ----------
ari = adjusted_rand_score(kmeans_labels, fcm_labels)
print(f"Adjusted Rand Index between K‑means and FCM: {ari:.4f}")

# ---------- Visualisation ----------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[1].imshow(kmeans_seg, cmap='nipy_spectral')
axes[1].set_title('K‑means Segmentation')
axes[2].imshow(fcm_seg, cmap='nipy_spectral')
axes[2].set_title('Fuzzy C‑means Segmentation')
plt.tight_layout()
plt.show()

# ---------- Boundary overlay ----------
# Find contours for each segmentation
contours_k = measure.find_contours(kmeans_seg, 0.5)
contours_f = measure.find_contours(fcm_seg, 0.5)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img_rgb)
for contour in contours_k:
    ax[0].plot(contour[:, 1], contour[:, 0], linewidth=2, color='red')
ax[0].set_title('K‑means boundaries')

ax[1].imshow(img_rgb)
for contour in contours_f:
    ax[1].plot(contour[:, 1], contour[:, 0], linewidth=2, color='blue')
ax[1].set_title('FCM boundaries')
plt.show()