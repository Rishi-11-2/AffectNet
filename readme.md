# AffectNet Image Extractor by Facial Expression

## Description
This Python script extracts images from the AffectNet dataset based on specified facial expression annotations. It helps in curating a subset of images representing a particular emotion (e.g., Happy, Sad, Angry) from the larger AffectNet dataset.

## Prerequisites
- Python 3.x
- NumPy library
- OpenCV-Python library
- AffectNet dataset (must be downloaded separately from the official source)

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:
   ```bash
   pip install numpy opencv-python
   ```
3. Download the AffectNet dataset. You will need both the images and the annotation files.

## Usage
1. **Clone or download this script (`a.py`) to your local machine.**
2. **Modify the script `a.py` to set the correct paths:**
   - Open `a.py` in a text editor.
   - Update the following path variables:
     - `DATA_PATH`: Set this to the absolute path of the directory containing the AffectNet `.npy` annotation files (e.g., `D:\Datasets\train_set\annotations`).
     - `DATA_PATH1`: Set this to the absolute path of the base directory of the AffectNet training set (e.g., `D:\Datasets\train_set`). The `images` folder should be inside this directory.
     - `directory`: Set this to the absolute path of the folder where you want to save the extracted images. This directory should correspond to the facial expression you intend to extract (e.g., `D:\Datasets\Happy_Images`).
   - **Specify the facial expression to extract:**
     - Locate the line `if value == 1:` in the script.
     - The numeric value (e.g., `1`) corresponds to a specific facial expression in AffectNet. You will need to refer to the AffectNet documentation to find the mapping for each expression (e.g., 0: Neutral, 1: Happy, 2: Sad, 3: Surprise, 4: Fear, 5: Disgust, 6: Anger, 7: Contempt). Change this value according to the expression you want to extract. For example, if "Anger" is `6`, change the line to `if value == 6:`.
3. **Run the script:**
   ```bash
   python a.py
   ```
4. The script will iterate through the images, check their annotations, and save the images matching the specified facial expression to the output `directory` you defined.

## Important Notes
   - The script currently uses an example path for loading a single annotation (`138_exp.npy`). This line is for understanding the path structure and is not strictly necessary for the script's core functionality if the main paths are set correctly.
   - The script includes commented-out lines for testing directory operations (`os.listdir()`, `os.chdir()`). These can be ignored or removed.
   - Ensure the output directory (specified in the `directory` variable) exists before running the script, or modify the script to create it if it doesn't exist.

## Contributing
Contributions to improve this script are welcome. Please fork the repository, make your changes, and submit a pull request.
