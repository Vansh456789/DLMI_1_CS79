# Medical Image Segmentation Assignments

This repository contains four projects on medical image segmentation, submitted as part of coursework. Each project explores different segmentation techniques and compares their performance.

## Projects Overview

1. **Brain MRI Tumor Segmentation** – Otsu vs Sauvola thresholding  
2. **White Blood Cell Segmentation** – K‑Means vs Fuzzy C‑Means clustering  
3. **Retinal Vessel Extraction** – Niblack vs Sauvola thresholding  
4. **Cell Nuclei Separation** – Marker‑controlled Watershed  

## Requirements

All code is written in Python 3.8+ and uses the libraries listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt


Datasets
Each project uses a publicly available dataset. Please download and place them as described below.

Project 2: White Blood Cell Segmentation
No specific dataset required. Place any blood cell image (e.g., from Wikimedia) in project2_wbc_segmentation/ and name it sample_blood_cell.jpg. Update the path in the code if needed.

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

text

---

## Final Steps for GitHub

1. Create the folder structure as shown above.
2. Place the code files in the respective folders (copy the code from this answer).
3. Download and place the datasets following the instructions.
4. Add the `requirements.txt` and `README.md` at the root.
5. Commit and push to GitHub.

If you prefer all projects as notebooks, you can simply rename the `.py` files to `.ipynb` after creating them in Jupyter (File → Download as → Notebook). Or you can keep both – it's up to you.

The code is designed to be self‑explanatory and easy to run, yet not overly simplistic – it demonstrates the core concepts while producing meaningful comparisons. Good luck with your submission!
