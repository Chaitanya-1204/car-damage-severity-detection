# 🚗 Car Damage Severity Detection

## 📁 Dataset Preparation

### 📥 Step 1: Download the Datasets

**Dataset 1**

```bash
curl -L "https://universe.roboflow.com/ds/5jiDOqp12h?key=F50PuQzUEA" -o roboflow.zip
unzip roboflow.zip -d dataset_1
rm roboflow.zip
```

**Dataset 2**

```bash
curl -L "https://universe.roboflow.com/ds/drLRwm9k8W?key=y30L1BJLAu" -o roboflow.zip
unzip roboflow.zip -d dataset_2
rm roboflow.zip
```

### 🔄 Step 2: Merge the Datasets

Run the following command to merge both datasets into a single formatted dataset:

```bash
python build_dataset.py
```

This script will:
1. Create JSON mappings of label names and their class indices for both datasets.
2. Generate a unified class mapping by merging and deduplicating class names.
3. Update all label files to use the new unified class indices.
4. Consolidate images and labels into a `final_dataset` directory.
5. Automatically generate a `data.yaml` file required for YOLO training.

### 🔧 Step 3: Clone the YOLOv5 Repository

```bash
git clone https://github.com/ultralytics/yolov5.git
```

Then choose your setup based on device availability:

**For CPU:**

```bash
cd yolov5
pip install -r requirements.txt
```

**For GPU (CUDA > 11.8 on Linux):**

1. Comment out `torch` and `torchvision` in `requirements.txt`.
2. Install them manually:

```bash
cd yolov5
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

3. Then install the rest:

```bash
pip install -r requirements.txt
```

### 🚀 Step 4: Train YOLOv5

Use the following script to begin training:

```bash
python train_yolov5_small_gpu.py
```