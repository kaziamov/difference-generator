from gendiff.scripts.parsing import get_format
from tests.paths import path

def test1():
    assert get_format('path/data.json') == '.json'
    assert get_format('./.gitignore') == ""
