# 画像比較 API

## API

### /get-color-avg

- 画像の画素値の平均を取得するための API
- 画像を 1 枚送信すると、その画像の画素値の平均を取得することができる

### /compare-image

- 予め設定しておいた画素値の平均と比較して、同じ画像かどうかを判定してくれる
- true なら同じ画像、false なら違う画像

## 使用言語

Python - Flask

## 環境構築

```
pip install opencv-python
pip install Flask

```
