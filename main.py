#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import datetime
import time
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

TRIALS = 2
TIME_AJUST = 0.070
SAVE_PATH = "./tmp"

def saveImage(image: Image.Image, filename: str):
    image.save(f"{SAVE_PATH}/{filename}.png")

def measure_process_time(process):
    time_start = time.time()
    process(TRIALS)
    time_elpsed = time.time() - time_start
    print(f"total:{format(time_elpsed,'.3f')}[s]\taverage:{format(time_elpsed/TRIALS,'.3f')}[s]")


def experiment_img_gen(trial):
    for i in range(trial):
        im = Image.effect_noise((640,480), 512)
        time.sleep(TIME_AJUST)

def experiment_simple(trial: int):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    for i in range(trial):
        im = Image.effect_noise((640,480), 512)
        # 画像生成と合わせて100msくらいに調整
        time.sleep(TIME_AJUST)
        saveImage(im, f"normal_{time_stamp}_{i}")

def experiment_multi_thread(trial: int):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for i in range(trial):
            im = Image.effect_noise((640,480), 512)
            # 画像生成と合わせて100msくらいに調整
            time.sleep(TIME_AJUST)
            executor.submit(saveImage, im, f"multi_thread_{time_stamp}_{i}")


if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

print(f"trials:{TRIALS}")

print(f"- execute:{experiment_img_gen.__name__}")
measure_process_time(experiment_img_gen)

print(f"- execute:{experiment_simple.__name__}")
measure_process_time(experiment_simple)

print(f"- execute:{experiment_multi_thread.__name__}")
measure_process_time(experiment_multi_thread)
