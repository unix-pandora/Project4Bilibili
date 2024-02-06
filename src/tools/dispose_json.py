import json
import chardet


def detect_encoding(file_path):
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())
    return result["encoding"]


def read_json_file(file_path):
    encode_type = detect_encoding(file_path)
    print("\n", "read_json_file encode_type: ", str(encode_type))

    with open(file_path, "r", encoding=encode_type, errors="ignore") as file:
        json_data = json.load(file)

    return json_data
