import json

def get_data(path):
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            return data
        else:
            return []
    except Exception:
        return []
