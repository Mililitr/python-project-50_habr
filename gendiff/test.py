from gendiff.parser import parse
from gendiff.generate_diff import make_diff
import json

filepath1 = '/home/hardduck/python-project-50/tests/fixtures/file1.json'
filepath2 = '/home/hardduck/python-project-50/tests/fixtures/file2.json'

data1 = parse(filepath1)
data2 = parse(filepath2)

diff = make_diff(data1, data2)
print(json.dumps(diff, indent =4))
