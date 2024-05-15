import os
import os.path

from curlywaffle.main import get_unique_file_path
from PIL import Image

dirname = os.path.dirname(__file__)

output_dir = f"{dirname}/processed"

base_img_dir = f"{dirname}/images"
img_subdirs = os.listdir(base_img_dir)

for img_subdir in img_subdirs:
    image_dir_path = f"{base_img_dir}/{img_subdir}"
    degrees_to_rotate = int(img_subdir)

    for file_name in os.listdir(image_dir_path):
        file_path = f"{image_dir_path}/{file_name}"
        if os.path.isdir(file_path) or file_path[-8:].lower() == '.gitkeep':
            continue

        output_file_path = get_unique_file_path(f"{output_dir}/{file_name}")

        try:
            with Image.open(file_path) as image:
                right_way_up = image.rotate(degrees_to_rotate, resample=None, expand=True)
                right_way_up.save(output_file_path)
                right_way_up.close()

        except (IOError, SyntaxError):
            print(f"Unable to rotate: {file_path}")
            continue