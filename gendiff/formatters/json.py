import json


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, tuple):
            return list(obj)
        return super().default(obj)


def format_diff_as_json(diff):
    return json.dumps(diff, ensure_ascii=False, separators=(',', ':'), sort_keys=True, cls=CustomEncoder).strip()
