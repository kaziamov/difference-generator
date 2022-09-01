from gendiff import functions

file1 = 'file1.json'
file2 = 'file2.json'

def test_generate_diff():
    assert functions.generate_diff(file1, file2) == result

