#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 04:17:35 2024


"""



import os
import pickle
from PIL import Image
import io

# Directory containing .tif files
directory = '/Users/leblapi1/Code/histopathologic-cancer-detection/test/'

# Find all .tif files in the directory
tif_files = [file for file in os.listdir(directory) if file.endswith('.tif')]

images_with_names = []

# Initialize the counter
counter = 0

for file_name in tif_files:
    with open(os.path.join(directory, file_name), 'rb') as file:
        img = Image.open(file)
        # Convert the image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='TIFF')
        # Store the filename and image bytes as a tuple
        images_with_names.append((file_name, img_bytes.getvalue()))
    
    counter += 1  # Increment the counter
    # Check if the counter is divisible by 1000
    if counter % 1000 == 0:
        print(f"Processing file number: {counter}")

# Pickle the list of (filename, image bytes) tuples
with open('test_images.pickle', 'wb') as pickle_file:
    pickle.dump(images_with_names, pickle_file)

