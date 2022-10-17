import json


def json_read(file: str):
    with open(file) as json_file:
        data = json.load(json_file)
        return data


def json_write(file: str, data):
    with open(file, 'w') as json_file:
        json.dump(data, json_file)
