<<<<<<< HEAD
Brain MRI Tumor Segmentation — Otsu vs Sauvola
📌 Objective

To compare global and adaptive thresholding methods for brain tumor segmentation in MRI images.

🧠 Methods Used

Otsu Thresholding (Global)

Sauvola Thresholding (Adaptive Local)

⚙️ Pipeline

Image preprocessing (Gaussian smoothing)

Global thresholding (Otsu)

Adaptive thresholding (Sauvola)

Morphological post-processing

Evaluation using Dice & Jaccard

📊 Evaluation Metrics

Dice Score

Jaccard Index (IoU)

📈 Observations

Otsu works well when tumor intensity is clearly separable.

Sauvola performs better in non-uniform intensity regions.

Post-processing improves both methods.

Adaptive thresholding handles intensity variation better.

📌 Conclusion

Adaptive thresholding (Sauvola) provides better segmentation in MRI images with uneven intensity distribution compared to global thresholding (Otsu).

=======
# DLMI_1_CS79
>>>>>>> 742473bbac31c6a2229b7b73138f3528659d1fe4
