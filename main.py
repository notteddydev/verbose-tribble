import os
import os.path

from curlywaffle.main import get_unique_file_path
from PIL import Image

output_dir = f"{os.getcwd()}/processed"

base_img_dir = f"{os.getcwd()}/images"
img_subdirs = os.listdir(base_img_dir)

for img_subdir in img_subdirs:
    image_dir_path = f"{base_img_dir}/{img_subdir}"
    degrees_to_rotate = int(img_subdir)

    for file_name in os.listdir(image_dir_path):
        file_path = f"{image_dir_path}/{file_name}"
        if os.path.isdir(file_path):
            continue

        output_file_path = get_unique_file_path(f"{output_dir}/{file_name}")

        with Image.open(file_path) as image:
            right_way_up = image.rotate(degrees_to_rotate, resample=None, expand=True)
            right_way_up.save(output_file_path)
            right_way_up.close()