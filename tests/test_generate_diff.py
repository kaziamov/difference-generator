from gendiff.scripts.gendiff import generate_diff
from tests.paths import path

def test1():
    file1 = path + 'flat_1.json'
    file2 = path + 'flat_2.json'
    filer = path + 'flat_r.txt'
    assert generate_diff(file1, file2) == open(filer, 'r').read()
    
    
def test2():
    file1 = path + 'flat_1.yaml'
    file2 = path + 'flat_2.yaml'
    filer = path + 'flat_r.txt'
    assert generate_diff(file1, file2) == open(filer, 'r').read()
    
    
def test3():
    file1 = path + 'flat_1.json'
    file2 = path + 'flat_2.yml'
    filer = path + 'flat_r.txt'
    assert generate_diff(file1, file2) == open(filer, 'r').read()