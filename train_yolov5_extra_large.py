# Training on multiple GPU's

import os

# Set environment variable for visible devices
os.environ["CUDA_VISIBLE_DEVICES"] = "0 , 1"

# Change to yolov5 directory
os.chdir("yolov5")

# Construct the DDP command
command = (
    "python -m torch.distributed.run --nproc_per_node=2 --master_port=12345 train.py "
    "--img 640 "
    "--batch 64 "
    "--epochs 200 "
    "--data ../data/data.yaml "
    "--weights yolov5x.pt "
    "--name yolov5_extra_large_epochs_200_lr_0.001_ "
    "--optimizer AdamW "
    "--workers 4 "
    "--project ../logs "
    "--patience 7 "
    "--hyp ../hyp-fine-tune.yaml "
    "--device 0,1 "
    "--seed 42 "
)

# Execute training
os.system(command)



# Construct the DDP command
command = (
    "python -m torch.distributed.run --nproc_per_node=2 --master_port=12345 train.py "
    "--img 640 "
    "--batch 64 "
    "--epochs 200 "
   "--data ../data/data.yaml "
    "--weights yolov5x.pt "
    "--name yolov5_extra_large_epochs_200_lr_0.0005_ "
    "--optimizer AdamW "
    "--workers 4 "
    "--project ../logs "
    "--patience 7 "
    "--hyp ../hyp-fine-tune_with_lr_0.0005.yaml "
    "--device 0,1 "
    "--seed 42 "
)

# Execute training
os.system(command)

