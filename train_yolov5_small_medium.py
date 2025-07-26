
# Training on single GPU 
import os
os.chdir("yolov5")

# os.system(
#     "python train.py "
#     "--img 640 "
#     "--batch 32 "
#     "--epochs 100 "
#     "--data ../data/data.yaml "
#     "--weights yolov5s.pt "
#     "--name yolov5_small "
#     "--optimizer AdamW "
#     "--device 3 "
#     "--workers 4 "
#     "--project ../logs "
#     "--patience 7 "  
#     "--hyp ../hyp-fine-tune.yaml "
#     "--seed 42 "
    
# )

# os.system(
#     "python train.py "
#     "--img 640 "
#     "--batch 32 "
#     "--epochs 100 "
#     "--data ../data/data.yaml "
#     "--weights yolov5m.pt "
#     "--name yolov5_medium "
#     "--optimizer AdamW "
#     "--device 3 "
#     "--workers 4 "
#     "--project ../logs "
#     "--patience 7 "  
#     "--seed 42 "
#     "--hyp ../hyp-fine-tune.yaml"
# )



os.system(
    "python train.py "
    "--img 640 "
   "--batch 64 "
    "--epochs 150 "
    "--data ../data/data.yaml "
    "--weights yolov5s.pt "
    "--name yolov5_small_lr_0005_epochs_150 "
    "--optimizer AdamW "
    "--device 3 "
    "--workers 4 "
    "--project ../logs "
    "--patience 7 "
    "--hyp ../hyp-fine-tune_with_lr_0.0005.yaml "
    "--seed 42 "
)

os.system(
    "python train.py "
    "--img 640 "
    "--batch 32 "
    "--epochs 150 "
    "--data ../data/data.yaml "
    "--weights yolov5m.pt "
    "--name yolov5_medium_lr_0005_epochs_150 "
    "--optimizer AdamW "
    "--device 3 "
    "--workers 4 "
    "--project ../logs "
    "--patience 7 "
    "--hyp ../hyp-fine-tune_with_lr_0.0005.yaml "
    "--seed 42 "
)

