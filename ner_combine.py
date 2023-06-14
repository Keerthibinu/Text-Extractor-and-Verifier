"""
Combine json files
"""
import json


def merge_json_files(file1, file2, output_file):
    """
        function
    """
    # Load data from file1
    with open(file1, 'r', encoding="utf-8") as file_1:
        data1 = json.load(file_1)

    # Load data from file2
    with open(file2, 'r', encoding="utf-8") as file_2:
        data2 = json.load(file_2)

    # Merge the annotations
    merged_data = {
        'annotations': data1['annotations'] + data2['annotations']
    }

    # Write merged data to the output file
    with open(output_file, 'w', encoding="utf-8") as outfile:
        json.dump(merged_data, outfile)


FILE1 = 'annotations.json'
FILE2 = 'training_data.json'
OUT = 'final.json'

merge_json_files(FILE1, FILE2, OUT)
