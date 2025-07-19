# Training on multiple GPU's

# import os

# # Set environment variable for visible devices
# os.environ["CUDA_VISIBLE_DEVICES"] = "1,3"

# # Change to yolov5 directory
# os.chdir("yolov5")

# # Construct the DDP command
# command = (
#     "python -m torch.distributed.run --nproc_per_node=2 --master_port=12345 train.py "
#     "--img 640 "
#     "--batch 16 "
#     "--epochs 100 "
#     "--data ../data/data.yaml "
#     "--weights yolov5s.pt "
#     "--name yolov5_small "
#     "--optimizer AdamW "
#     "--workers 4 "
#     "--project ../logs "
#     "--patience 5 "
#     "--device 0,1"
# )

# # Execute training
# os.system(command)


# Training on single GPU 
import os
os.chdir("yolov5")

os.system(
    "python train.py "
    "--img 640 "
    "--batch 64 "
    "--epochs 20 "
    "--data ../data/data.yaml "
    "--weights yolov5s.pt "
    "--name yolov5_small "
    "--optimizer AdamW "
    "--device 3 "
    "--workers 4 "
    "--project ../logs "
    "--patience 3"  
)