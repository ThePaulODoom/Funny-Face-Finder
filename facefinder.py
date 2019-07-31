"""
pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
"""
import face_recognition as face
import os
from PIL import Image

image_files = []

for root, dirs, files in os.walk(".\input"):
    for x in files:
        if not x.endswith("zip"):
            image_files.append(os.path.join(root, x))

for file in image_files:
    try:
        i = 0
        im = face.load_image_file(file)
        coords = face.face_locations(im)
        file_name = file.split("\\")[len(file.split("\\"))-1]
        if len(coords) == 0:
            print(f"{file_name} : There were no faces found in this picture")
        else:
            print(f"{file_name} : There were {len(coords)} face(s) found in this picture")
        for coord in coords:
            i += 1
            up = coord[0]
            right = coord[1]
            down = coord[2]
            left = coord[3]
            img = Image.open(file)
            crop = img.crop((left,up,right,down))
            name = file.split("\\")
            name = name[len(name)-1]
            name = name.split(".")
            name = name[0] + str(i) + "." + name[1]
            name = "".join(name.split())
            crop.save(f".\output\{name}")
    except:
        continue
