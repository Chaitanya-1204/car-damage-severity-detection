from data_utils.generate_class_map import get_mapping
from data_utils.sync_label_indices import sync_labels
from data_utils.merge_dataset import merge

get_mapping()
sync_labels()
merge()