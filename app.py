from cv2 import mean
from flask import Flask, request
from werkzeug.utils import  secure_filename
import os
import cv2

app = Flask(__name__)

@app.route("/get-color-avg", methods=["GET", "POST"])
def get_color_avg():
    if request.method == "POST":

        file = request.files["image"] # 画像の取得
        filename = secure_filename(file.filename) # ファイル名の変換
        filepath = os.path.join("./images", filename) # 画像の保存先パスを生成
        file.save(filepath) # 画像の保存

        pixel_value = cv2.imread(filepath).mean(0).mean(0) # 画素値の平均を取得
    
    return {"color_avg" : [pixel_value[0], pixel_value[1], pixel_value[2]]}


@app.route("/compare-image", methods=["GET", "POST"])
def compare_image():

    file = request.files["image"] # 画像の取得
    filename = secure_filename(file.filename) # ファイル名の変換
    filepath = os.path.join("./images", filename) # 画像の保存先パスを生成
    file.save(filepath) # 画像の保存
        
    # ここに/get-color-avgで取得した値を入力する
    image_value = [219.39070550931422, 219.39070550931422, 219.39070550931422]
        

    pixel_value = cv2.imread(filepath).mean(0).mean(0) # 画素値の平均を取得
    diff_value = []
        
    # 画素値を比較
    for i,num in enumerate(image_value):
        diff_value.append(int(num - pixel_value[i]))
    
    is_same = False
    
    # 画像の違いを判定    
    if int(sum(diff_value) / 3) == 0:
        is_same = True
    
            
    return {"same_image" : is_same}

if __name__ == "__main__":
    app.run(debug=True)
