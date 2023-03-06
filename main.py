#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import datetime
import time
import os

def saveImage(image: Image.Image,path: str, filename: str):
    time_stamp = datetime.datetime.now()
    if not os.path.exists(path):
        os.makedirs("./"+path)
    image.save(f"./{path}/{time_stamp.strftime('%Y%m%d%H%M%S%f')}_{filename}.png")

for i in range(10):
    time_start = time.time()
    im = Image.effect_noise((640,480), 512)
    time_gen = time.time() - time_start

    time_start = time.time()
    saveImage(im, "tmp", "test")
    time_save = time.time() - time_start

    print(f"gen:{format(time_gen, '.3f')}\tsave:{format(time_save,'.3f')}")
