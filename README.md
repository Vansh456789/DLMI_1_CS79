# 📌 Medical Image Segmentation — Classical Approaches

This repository contains four structured academic projects exploring **classical image segmentation techniques** applied to biomedical image analysis tasks.  
All implementations follow the assigned coursework requirements, using traditional image processing and computer vision methods — **no deep learning**.

---

## 📂 Repository Structure

Medical-Image-Segmentation

### 🔹 Project-1-Brain-MRI
- `brain_mri_segmentation.ipynb`
- Tumor segmentation using Otsu vs Sauvola
- Evaluation: Dice & Jaccard

### 🔹 Project-2-WBC-Clustering
- `wbc_segmentation_kmeans_fcm.ipynb`
- K-Means vs Fuzzy C-Means clustering
- Boundary comparison & ARI metric

### 🔹 Project-3-Retinal-Vessel
- `retinal_vessel_extraction.ipynb`
- Niblack vs Sauvola thresholding
- Vessel sensitivity analysis

### 🔹 Project-4-Nuclei-Watershed
- `nuclei_separation_watershed.ipynb`
- Watershed with vs without markers
- Over-segmentation comparison

---

Each project follows a consistent workflow:
1. Dataset loading  
2. Preprocessing  
3. Algorithm implementation  
4. Metric evaluation  
5. Visualization  
6. Conclusion


### Structure Explanation

- **Project-1-Brain-MRI**  
  Global vs adaptive thresholding (Otsu vs Sauvola) with Dice & Jaccard evaluation.

- **Project-2-WBC-Clustering**  
  Hard vs soft clustering (K-Means vs Fuzzy C-Means) for WBC segmentation.

- **Project-3-Retinal-Vessel**  
  Local thresholding comparison (Niblack vs Sauvola) on DRIVE dataset.

- **Project-4-Nuclei-Watershed**  
  Marker-controlled watershed vs normal watershed to analyze over-segmentation.

Each project is independently executable and follows a consistent workflow:
1. Data loading  
2. Preprocessing  
3. Method implementation  
4. Evaluation  
5. Visualization  
6. Conclusion


Each project folder contains a Kaggle Jupyter Notebook that:
- Implements specified methods
- Compares results according to task requirements
- Uses dataset-level evaluation where applicable
- Includes visual examples and interpretation

---

## 🧠 Project Descriptions

---

### 🧠 **Project 1 — Brain MRI Tumor Segmentation**

**Objective:** Segment tumor regions from Brain MRI scans using thresholding.  
**Methods Compared:**  
- Global Thresholding — Otsu  
- Adaptive Thresholding — Sauvola  

**Evaluation Metrics:**  
- Dice Coefficient  
- Jaccard Index (IoU)

**Dataset:**  
📌 *Brain Tumor Segmentation (Kaggle)*  
https://www.kaggle.com/datasets/nikhilroxtomar/brain-tumor-segmentation

**Highlights:**
- Demonstrates global vs local segmentation behavior
- Quantitative evaluation across the dataset
- Visual and metric comparison

---

### 🧫 **Project 2 — White Blood Cell Segmentation**

**Objective:** Segment the nucleus and cytoplasm regions in white blood cell images.  
**Methods Compared:**  
- K-Means Clustering (hard clustering)  
- Fuzzy C-Means Clustering (soft clustering)  

**Evaluation Metric:**  
- Adjusted Rand Index (ARI) for clustering similarity

**Dataset:**  
📌 *Blood Cells (Kaggle)*  
https://www.kaggle.com/datasets/paultimothymooney/blood-cells

**Highlights:**
- Color feature-space segmentation
- Hard vs soft clustering comparison
- Dataset-level evaluation with ARI

---

### 👁️ **Project 3 — Retinal Vessel Extraction**

**Objective:** Extract blood vessels from retinal fundus images.  
**Methods Compared:**  
- Niblack Local Thresholding  
- Sauvola Local Thresholding  

**Primary Evaluation Metric:**  
- Sensitivity (True Positive Rate)

**Dataset:**  
📌 *DRIVE — Digital Retinal Images for Vessel Extraction (Kaggle)*  
https://www.kaggle.com/datasets/andrewmvd/drive-digital-retinal-images-for-vessel-extraction

**Highlights:**
- Uses green channel for enhanced contrast
- Local adaptive thresholding for thin structures
- Sensitivity computed over entire dataset

---

### 🧫 **Project 4 — Cell Nuclei Separation**

**Objective:** Separate touching nuclei in microscopy images.  
**Methods Compared:**  
- Watershed without markers  
- Marker-controlled watershed

**Learning Focus:**  
- Over-segmentation control  
- Distance transform seed detection

**Dataset:**  
📌 *Data Science Bowl 2018 – Nuclei Segmentation (Kaggle)*  
https://www.kaggle.com/datasets/mahmudulhasantasin/data-science-bowl-2018-competition-merged-mask

**Highlights:**
- Distance transform to find identifying peaks
- Comparison with & without marker control
- Visualization of separation behavior

---

## 🛠 Techniques and Tools

This repository uses:

- **Python**
- **OpenCV** for image processing
- **NumPy** for array manipulation
- **Scikit-image** for segmentation utilities
- **Scikit-Learn / scikit-fuzzy** where applicable
- **Matplotlib** for visualization

All core segmentation logic is implemented with classical algorithms — no machine learning or deep learning models are used.

---

## 📈 What You Will Learn

These projects build a foundation in:

✔ Global vs adaptive thresholding  
✔ Hard vs soft clustering behavior  
✔ Local thresholding for thin structures  
✔ Distance transform & watershed segmentation  
✔ Computation of segmentation metrics  
✔ Dataset-level evaluation and comparison  
✔ Visual interpretation of results

Each notebook is independently executable and includes:
- Step-by-step implementation
- Visual results and comparison
- Metric calculation matching assignment requirements

---

## 📌 Important Notes

- Each project follows the exact methods specified in the assignment sheet.
- Evaluations are performed over full datasets where required.
- Figures and results are included in the notebooks for clarity.

---

## 🔗 Dataset References

- **Brain Tumor Segmentation (Kaggle):**  
  https://www.kaggle.com/datasets/nikhilroxtomar/brain-tumor-segmentation

- **Blood Cells (Kaggle):**  
  https://www.kaggle.com/datasets/paultimothymooney/blood-cells

- **DRIVE Retinal Vessel Dataset (Kaggle):**  
  https://www.kaggle.com/datasets/andrewmvd/drive-digital-retinal-images-for-vessel-extraction

- **Data Science Bowl 2018 Cell Nuclei (Kaggle):**  
  https://www.kaggle.com/datasets/mahmudulhasantasin/data-science-bowl-2018-competition-merged-mask

---

## 📌 Contact

For questions or further clarifications, feel free to file an issue or contact the repository maintainer.

---

project2_wbc_segmentation/ and name it sample_blood_cell.jpg. Update the path in the code if needed.

Project 3: Retinal Vessel Extraction
Download the DRIVE dataset from Kaggle.

Extract the zip and place the DRIVE folder inside project3_retinal_vessel/. The expected structure:

text
project3_retinal_vessel/DRIVE/training/images/21_training.tif
Project 4: Cell Nuclei Separation
Download the 2018 Data Science Bowl dataset from Kaggle.

Extract stage1_train.zip into project4_cell_nuclei/data-science-bowl-2018/. The folder should contain subfolders like 0a7d30b... with images/ and masks/.

Running the Code
Each project folder contains both a Python script (.py) and a Jupyter notebook (.ipynb). You can run either:

bash
cd projectX_.../
python script_name.py
or open the notebook in Jupyter and run all cells.

The code will display the segmentation results and print quantitative metrics where applicable.

Results Summary
Project 2: Adjusted Rand Index measures similarity between hard and soft clustering.

Project 3: Dice and Jaccard scores compare Niblack and Sauvola against ground truth.

Project 4: Number of segmented regions shows how marker control reduces over‑segmentation.

License
This repository is for educational purposes only. The datasets belong to their respective owners.
