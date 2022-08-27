from cv2 import mean
from flask import Flask, request
from werkzeug.utils import  secure_filename
import os
import cv2

app = Flask(__name__)

@app.route("/get-color-avg", methods=["GET", "POST"])
def get_color_avg():
    if request.method == "POST":

        file = request.files["image"]
        filename = secure_filename(file.filename)
        filepath = os.path.join("./images", filename)
        file.save(filepath)

        pixel_value = cv2.imread(filepath).mean(0).mean(0)
        print(pixel_value)
    
    return {"color_avg" : [pixel_value[0], pixel_value[1], pixel_value[2]]}


@app.route("/compare-image", methods=["GET", "POST"])
def compare_image():
    if request.method == "POST":

        file = request.files["image"]
        filename = secure_filename(file.filename)
        filepath = os.path.join("./images", filename)
        file.save(filepath)
        
        image_value = [219.39070550931422,
        219.39070550931422,
        219.39070550931422]
        
        pixel_value = cv2.imread(filepath).mean(0).mean(0)
        diff_value = []
        
        for i,num in enumerate(image_value):
            diff_value.append(int(num - pixel_value[i]))
        
        is_same = False
        
        if int(sum(diff_value) / 3) == 0:
            is_same = True
    
            
    return {"same_image" : is_same}

if __name__ == "__main__":
    app.run(debug=True)
