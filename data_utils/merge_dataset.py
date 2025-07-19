import os
import shutil
from pathlib import Path

import json
import yaml


def copy_dataset_contents(source_root, target_root):
    """
    Copy images and labels from source dataset directories to the target directory,
    reorganizing the structure according to the specified split mapping.
    """
    split_mapping = {'train': 'train', 'test': 'test', 'valid': 'val'}

    for split, final_split in split_mapping.items():
        for content_type in ['images', 'labels']:
            src_dir = os.path.join(source_root, split, content_type)
            dst_dir = os.path.join(target_root, content_type, final_split)

            # Create destination dir if not exists
            os.makedirs(dst_dir, exist_ok=True)

            # Copy all files
            for file in os.listdir(src_dir):
                src_file = os.path.join(src_dir, file)
                dst_file = os.path.join(dst_dir, file)
                shutil.copy2(src_file, dst_file)
                # print(f"Copied {src_file} -> {dst_file}")
    print(f"Copied contents from {source_root} to {target_root}")


def create_yaml_from_combined_json(combined_json_path, output_yaml_path):
    """
    Create a YAML configuration file from a combined JSON class mapping,
    including train, val, test paths, number of classes, and class names.
    """
    with open(combined_json_path, 'r') as f:
        combined = json.load(f)

    # Sort by index
    sorted_items = sorted(combined.items(), key=lambda item: item[1])
    sorted_names = [name for name, _ in sorted_items]
    nc = len(sorted_names)

    with open(output_yaml_path, 'w') as f:
        # Write dataset paths and class info to YAML
        f.write(f"train: ../data/images/train\n")
        f.write(f"val: ../data/images/val\n")
        f.write(f"test: ../data/images/test\n\n")
        f.write(f"nc: {nc}\n")
        f.write("names: [")
        f.write(", ".join(f"'{name}'" for name in sorted_names))
        f.write("]\n")
    print(f"YAML file created at {output_yaml_path}")
    
    

def merge():
    # Define base directory relative to this script
    base_dir = Path(__file__).resolve().parent.parent

    # Define source and target dataset directories
    dataset_1 = base_dir / "dataset_1"
    dataset_2 = base_dir / "dataset_2"
    final_dataset = base_dir / "data"

    # Copy dataset contents from both datasets into final dataset directory
    copy_dataset_contents(dataset_1, final_dataset)
    copy_dataset_contents(dataset_2, final_dataset)

    # Create YAML file from combined class mapping JSON
    combined_json_path = base_dir/"class_mappings" / "combined.json"
    yaml_output_path = final_dataset / "data.yaml"
    create_yaml_from_combined_json(combined_json_path, yaml_output_path)

    # Cleanup: Delete the original dataset directories
    shutil.rmtree(dataset_1)
    shutil.rmtree(dataset_2)
    print("Deleted dataset_1 and dataset_2 directories.")
   