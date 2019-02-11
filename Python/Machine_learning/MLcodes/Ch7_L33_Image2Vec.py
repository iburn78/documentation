from PIL import Image
import numpy as np

with open("tower.jpg", "rb") as file: 
    img = Image.open(file)
    img = img.convert("RGB")
    img = img.resize((64,64))
    data = np.asarray(img)
    img.save("tower_RGB.png")

    print(len(list(data)), len(data[0]), data[0][0])
