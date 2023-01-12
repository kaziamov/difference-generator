import os
import pytest
import json

def fixtures_path(path):
    return os.path.join(os.path.dirname(__file__), 'fixtures/', path, '{}').format


flat_dir = fixtures_path('flat/')
tree_dir = fixtures_path('tree/')
expected_dir = fixtures_path('expected/')


flat_expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


with open(expected_dir('tree_expected.txt'), 'r', encoding='utf-8') as file:
    tree_expected = file.read()

flat_fixtures = [
    (flat_dir('flat_1.json'), flat_dir('flat_2.yaml'), flat_expected),
]

tree_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.yaml'), tree_expected),
]
'{\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: null\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n              - wow: \n              + wow: so much\n            key: value\n          + ops: vops\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n}'
'{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: null\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n        setting6: {\n            doge: {\n              - wow: \n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n}'

{'status': 'root', 'child': [{'key': 'common', 'status': 'child', 'child': [{'key': 'follow', 'status': 'added', 'value': False}, {'key': 'setting1', 'status': 'same', 'value': 'Value 1'}, {'key': 'setting2', 'status': 'removed', 'value': 200}, {'key': 'setting3', 'status': 'updated', 'value': True, 'value2': None}, {'key': 'setting4', 'status': 'added', 'value': 'blah blah'}, {'key': 'setting5', 'status': 'added', 'value': {'key5': 'value5'}}, {'key': 'setting6', 'status': 'child', 'child': [{'key': 'doge', 'status': 'child', 'child': [{'key': 'wow', 'status': 'updated', 'value': '', 'value2': 'so much'}]}, {'key': 'key', 'status': 'same', 'value': 'value'}, {'key': 'ops', 'status': 'added', 'value': 'vops'}]}]}, {'key': 'group1', 'status': 'child', 'child': [{'key': 'baz', 'status': 'updated', 'value': 'bas', 'value2': 'bars'}, {'key': 'foo', 'status': 'same', 'value': 'bar'}, {'key': 'nest', 'status': 'updated', 'value': {'key': 'value'}, 'value2': 'str'}]}, {'key': 'group2', 'status': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'key': 'group3', 'status': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]}