import os


def fixtures_path(path):
    return os.path.join(os.path.dirname(__file__), 'fixtures/', path, '{}').format


tree_dir = fixtures_path('tree/')
expected_dir = fixtures_path('expected/')


with open(expected_dir('tree_expected.txt'), 'r', encoding='utf-8') as file:
    tree_expected = file.read()

tree_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.json'), tree_expected),
    (tree_dir('tree_1.yml'), tree_dir('tree_2.yaml'), tree_expected)]


with open(expected_dir('tree_plain_expected.txt'), 'r', encoding='utf-8') as file:
    tree_plain_expected = file.read()

tree_plain_fixtures = [
    (tree_dir('tree_1.json'), tree_dir('tree_2.json'), tree_plain_expected),
    (tree_dir('tree_1.yml'), tree_dir('tree_2.yaml'), tree_plain_expected)]
