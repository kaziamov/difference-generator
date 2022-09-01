from gendiff import functions

file1 = 'file1.json'
file2 = 'file2.json'

def test_create_set():
    assert functions.create_set([1, 2, 3, 4]) == {1, 2, 3, 4}
    assert functions.create_set([1, 2, 3, 3, 2, 4]) == {1, 2, 3, 4}
    assert functions.create_set(['a', 'b']) == {'a', 'b'}
    assert functions.create_set({'a': 1, 'b': 2, 'c': 3}) == {'a', 'b', 'c'}

# def test_generate_diff():
#     assert functions.generate_diff(file1, file2) == result

