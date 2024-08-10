import numpy as np
import os
import cv2 as cv

a = np.load(
    "D:\Datasets\\train_set\\annotations\\138_exp.npy"
)  # example of how the path of an image label look

print(type(a))

DATA_PATH = "D:\Datasets\\train_set\\annotations"  # full path for the training dataset

DATA_PATH1 = "D:\Datasets\\train_set"

IMAGE_PATH = os.path.join(DATA_PATH1, "images")

directory = (
    "D:\Datasets\\Happy"  # to be changed accordingly depends on the type images  of the facial expressions  we need
)

# Some testing. to be commented out while running the actual code
# os.listdir()
# os.chdir(directory)
# os.listdir()
# os.chdir(IMAGE_PATH)
# os.listdir()


for file in os.listdir(IMAGE_PATH):
    f = file
    file = file[:-4]
    try:
        value = np.load(os.path.join(DATA_PATH, "{}_exp.npy".format(file)))
        img = cv.imread(os.path.join(IMAGE_PATH, f))
        value = (int)(value.item())
        # print(img)
        if value == 1:
            os.chdir(directory)
            cv.imwrite(f, img)
            os.chdir(IMAGE_PATH)
    except:
        pass
