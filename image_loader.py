import cv2
import os

def validate_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full path to the image
            file_path = os.path.join(root, file)

            # Attempt to load the image
            image = cv2.imread(file_path)

            # Check if the image was loaded successfully
            if image is not None:
                continue
            else:
                print(file_path)

directory = 'image_data'  # Replace with the path to your directory
validate_images(directory)
