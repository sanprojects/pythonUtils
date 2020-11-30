import json


def load(fn):
    try:
        # return yaml.safe_load(open(fn, "r")) or {}
        return json.load(open(fn, "r")) or {}
    except:
        return {}


def save(fn, data):
    with open(fn, "w") as file:
        # file.write(yaml.dump(data))
        json.dump(data, file, ensure_ascii=False, indent=4)

