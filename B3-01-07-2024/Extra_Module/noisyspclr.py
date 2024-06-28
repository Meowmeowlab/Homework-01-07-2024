import os
import cv2
import numpy as np
import random

def add_sp_clr(image, noise_percent: float):
    # Load the image
    #load_path = os.path.join('.','b1', 'img', 'cat_superlowres.jpg')
    #image = cv2.imread(load_path)

    # Specify the percentage of pixels affected by noise
    # noise_percent = 0.02  # 2%

    # Create a copy of the image to work with
    sp_noisy_image = image.copy()

    # Get the dimensions of the image
    height, width, channels = image.shape

    # Calculate the number of pixels to alter
    num_noise_pixels = int(height * width * noise_percent)

    for i in range(num_noise_pixels):
        # Randomly choose a pixel
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)

        # Randomly choose a value (salt or pepper)
        value = random.choice([0, 255])

        # Apply the noise (for grayscale, remove the loop)
        for c in range(channels):
            sp_noisy_image[y, x, c] = value

    # Save or display the image
    # save_path = os.path.join('.','b1', 'img', 'cat_superlowres_sp.jpg')
    # cv2.imwrite(save_path, sp_noisy_image)
    # cv2.imshow("test",sp_noisy_image)
    # cv2.waitKey(0)
    return sp_noisy_image
