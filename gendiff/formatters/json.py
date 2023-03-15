import json


def format_diff_as_json(diff):
    return json.dumps(diff, indent=2)
