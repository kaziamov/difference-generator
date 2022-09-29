from gendiff.scripts.parsing import read_and_parse
from tests.paths import path

def test_1():
    file = path + 'flat_1.json'
    result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert read_and_parse(file) == result

def test_2():
    file = path + 'flat_2.json'
    result = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert read_and_parse(file) == result