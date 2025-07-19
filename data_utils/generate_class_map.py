import os
import yaml
import json


def load_names(yaml_path):
    """Load class names from a YOLO data.yaml file."""
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get("names", [])


def get_mapping():
    # Paths to dataset YAMLs
    yaml_paths = {
        "dataset_1": "dataset_1/data.yaml",
        "dataset_2": "dataset_2/data.yaml"
    }

    # Load class names from each dataset
    dataset_names = {
        key: load_names(path)
        for key, path in yaml_paths.items()
    }

    # Generate class index mappings for dataset_1 and dataset_2
    dataset_jsons = {
        "dataset_1.json": {idx: name for idx, name in enumerate(dataset_names["dataset_1"])},
        "dataset_2.json": {idx: name for idx, name in enumerate(dataset_names["dataset_2"])}
    }

    # Build combined mapping (deduplicated), preserving dataset_1 indices
    combined_json = {
        name: idx for idx, name in enumerate(dataset_names["dataset_1"])
    }
    next_idx = len(combined_json)
    for name in dataset_names["dataset_2"]:
        if name not in combined_json:
            combined_json[name] = next_idx
            next_idx += 1

    # Sort combined mapping by index
    combined_json = dict(sorted(combined_json.items(), key=lambda x: x[1]))

    # Save all mappings to JSON files
    output_dir = "class_mappings"
    os.makedirs(output_dir, exist_ok=True)

    for filename, data in dataset_jsons.items():
        with open(os.path.join(output_dir, filename), 'w') as f:
            json.dump(data, f, indent=2)

    with open(os.path.join(output_dir, "combined.json"), 'w') as f:
        json.dump(combined_json, f, indent=2)

    print("Saved the following files to 'class_mappings/' directory:\n"
          "- dataset_1.json\n"
          "- dataset_2.json\n"
          "- combined.json")