from gendiff.scripts.gendiff import generate_diff
from tests.paths import path

def test1():
    file1 = path + 'flat_1.json'
    file2 = path + 'flat_2.json'
    filer = path + 'flat_r.txt'
    assert generate_diff(file1, file2) == open(filer, 'r').read()