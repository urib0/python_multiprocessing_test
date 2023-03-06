#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import datetime
import time
import os

TRIALS = 20
TIME_AJUST = 0.070
SAVE_PATH = "./tmp"

def saveImage(image: Image.Image,path: str, filename: str):
    time_stamp = datetime.datetime.now()
    image.save(f"{path}/{time_stamp.strftime('%Y%m%d%H%M%S%f')}_{filename}.png")

def experiment_img_gen(trial):
    for i in range(trial):
        im = Image.effect_noise((640,480), 512)
        time.sleep(TIME_AJUST)

def experiment_simple(trial: int):
    for i in range(trial):
        im = Image.effect_noise((640,480), 512)
        # 画像生成と合わせて100msくらいに調整
        time.sleep(TIME_AJUST)
        saveImage(im, SAVE_PATH, i)

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

print(f"trials:{TRIALS}")

time_start = time.time()
experiment_img_gen(TRIALS)
time_ex_img_gen = time.time() - time_start
print(f"ex_img_gen:{format(time_ex_img_gen,'.3f')}\taverage:{format(time_ex_img_gen/TRIALS,'.3f')}")

time_start = time.time()
experiment_simple(TRIALS)
time_ex_simple = time.time() - time_start
print(f"ex_simple:{format(time_ex_simple,'.3f')}\t\taverage:{format(time_ex_simple/TRIALS,'.3f')}")

