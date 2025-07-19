import json
import os

def update_labels(dataset_map, combined_map, labels_dir):
    """Update label files in labels_dir by mapping old indices to new indices based on combined_map."""
    class_to_combined_index = {k: v for k, v in combined_map.items()}

    for filename in os.listdir(labels_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(labels_dir, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if not parts:
                    continue
                old_index = parts[0]
                class_name = dataset_map.get(old_index)
                if class_name is None:
                    print(f"Warning: Unknown class index {old_index} in file {filename}")
                    continue
                new_index = class_to_combined_index.get(class_name)
                if new_index is None:
                    print(f"Warning: Class name {class_name} not in combined mapping")
                    continue
                parts[0] = str(new_index)
                updated_lines.append(' '.join(parts))

            with open(file_path, 'w') as f:
                f.write('\n'.join(updated_lines))


def update_dataset_1_labels(dataset_1_json_path, combined_json_path, labels_dir):
    """Update dataset 1 label files with new indices from the combined mapping."""
    with open(dataset_1_json_path, 'r') as f:
        dataset1_map = json.load(f)

    with open(combined_json_path, 'r') as f:
        combined_map = json.load(f)

    update_labels(dataset1_map, combined_map, labels_dir)


def update_dataset_2_labels(dataset_2_json_path, combined_json_path, labels_dir):
    """Update dataset 2 label files with new indices from the combined mapping."""
    with open(dataset_2_json_path, 'r') as f:
        dataset2_map = json.load(f)

    with open(combined_json_path, 'r') as f:
        combined_map = json.load(f)

    update_labels(dataset2_map, combined_map, labels_dir)


def sync_labels():
    # Dataset 1
    for subset in ["train", "test", "valid"]:
        update_dataset_1_labels(
            dataset_1_json_path="class_mappings/dataset_1.json",
            combined_json_path="class_mappings/combined.json",
            labels_dir=f"dataset_1/{subset}/labels"
        )

    # Dataset 2
    for subset in ["train", "test", "valid"]:
        update_dataset_2_labels(
            dataset_2_json_path="class_mappings/dataset_2.json",
            combined_json_path="class_mappings/combined.json",
            labels_dir=f"dataset_2/{subset}/labels"
        )

    

    