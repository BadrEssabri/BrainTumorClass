import h5py
import glob
import re
import matplotlib.pyplot as plt
import numpy as np
import cv2

folder_path = "./new-data-raw/*.h5"  # Replace with the actual folder path and file extension pattern

# Get a list of file paths
file_paths = glob.glob(folder_path)

# Loop over the files
count = 0
threshold = 400
for file_path in file_paths:
    match = re.search(r'slice_(\d+)', file_path)
    index = match.group(1)

    # Open the H5 file
    if (int(index) > 50 and int(index) <110):
        with h5py.File(file_path, "r") as f:
            #only take the T1 weight post contrast
            image_brain = f["image"][()][:,:,1]
            mask_brain = f["mask"][()]

            pixel_count = np.sum(mask_brain)
            if np.sum(mask_brain) > threshold:
                plt.imshow(image_brain, cmap='gray')
                plt.axis('off')
                plt.savefig(f"./new-data-processed/tumor_image_{count}.jpg", bbox_inches='tight', pad_inches=0)

                count += 1
                plt.show()

print("Done")