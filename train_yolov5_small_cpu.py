# train_yolov5.py
import os
os.chdir("yolov5")

os.system(
    "python train.py "
    "--img 640 "
    "--batch 16 "
    "--epochs 100 "
    "--data ../data/data.yaml "
    "--weights yolov5s.pt "
    "--name yolov5_small "
    "--optimizer AdamW "
    "--device 3 "
    "--workers 4 "
    "--project ../logs "
    "--patience 5"  
)