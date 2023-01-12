import os
import pytest
import json

def fixtures_path(path):
    return os.path.join(os.path.dirname(__file__), 'fixtures/', path, '{}').format


flat_dir = fixtures_path('flat/')
tree_dir = fixtures_path('tree/')
expected_dir = fixtures_path('expected/')


with open(expected_dir('flat_expected.txt'), 'r', encoding='utf-8') as file:
    flat_expected = file.read()

with open(expected_dir('flat_plain_expected.txt'), 'r', encoding='utf-8') as file:
    flat_plain_expected = file.read()

with open(expected_dir('tree_expected.txt'), 'r', encoding='utf-8') as file:
    tree_expected = file.read()

with open(expected_dir('tree_plain_expected.txt'), 'r', encoding='utf-8') as file:
    tree_plain_expected = file.read()


flat_fixtures = [
    (flat_dir('flat_1.yaml'), flat_dir('flat_2.yml'), flat_expected),
    (flat_dir('flat_1.json'), flat_dir('flat_2.json'), flat_expected),
]
flat_plain_fixtures = [
    (flat_dir('flat_1.yaml'), flat_dir('flat_2.yml'), flat_plain_expected),
    (flat_dir('flat_1.json'), flat_dir('flat_2.json'), flat_plain_expected),
]

tree_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.json'), tree_expected),
    (tree_dir('tree_1.yml'), tree_dir('tree_2.yaml'), tree_expected),
]
tree_plain_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.json'), tree_plain_expected),
    (tree_dir('tree_1.yml'), tree_dir('tree_2.yaml'), tree_plain_expected),
]
