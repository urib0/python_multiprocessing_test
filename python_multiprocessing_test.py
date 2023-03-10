#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import datetime
import time
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

TRIALS = 100
TIME_AJUST_GEN = 0.070
TIME_AJUST_SAVE = 0.020
SAVE_PATH = "./tmp"
IMAGE_SIZE = (640,480)

def saveImage(image: Image.Image, filename: str):
    image.save(f"{SAVE_PATH}/{filename}.png")
    time.sleep(TIME_AJUST_SAVE)

def measure_process_time(process):
    time_start = time.time()
    process(TRIALS)
    time_elpsed = time.time() - time_start
    print(f"total:{format(time_elpsed,'.4f')}[s]\taverage:{format(time_elpsed/TRIALS,'.4f')}[s]")


def experiment_img_gen(trial):
    for i in range(trial):
        im = Image.effect_noise(IMAGE_SIZE, 512)
        time.sleep(TIME_AJUST_GEN)

def experiment_simple(trial: int):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    for i in range(trial):
        im = Image.effect_noise(IMAGE_SIZE, 512)
        time.sleep(TIME_AJUST_GEN)
        saveImage(im, f"normal_{time_stamp}_{i}")

def experiment_multi_thread(trial: int):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for i in range(trial):
            im = Image.effect_noise(IMAGE_SIZE, 512)
            time.sleep(TIME_AJUST_GEN)
            executor.submit(saveImage, im, f"multi_thread_{time_stamp}_{i}")

def experiment_multi_process(trial: int):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        for i in range(trial):
            im = Image.effect_noise(IMAGE_SIZE, 512)
            time.sleep(TIME_AJUST_GEN)
            executor.submit(saveImage, im, f"multi_process_{time_stamp}_{i}")


if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

print(f"trials:{TRIALS}")

print(f"- execute:{experiment_img_gen.__name__}")
measure_process_time(experiment_img_gen)

print(f"- execute:{experiment_simple.__name__}")
measure_process_time(experiment_simple)

print(f"- execute:{experiment_multi_thread.__name__}")
measure_process_time(experiment_multi_thread)

print(f"- execute:{experiment_multi_process.__name__}")
measure_process_time(experiment_multi_process)
