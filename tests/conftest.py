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
    (flat_dir('flat_1.yaml'), flat_dir('flat_2.yml'), flat_expected),
]

tree_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.yaml'), tree_expected),
    (tree_dir('tree_1.yml'), tree_dir('tree_2.yaml'), tree_expected),
]
