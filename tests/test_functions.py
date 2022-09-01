from gendiff import functions


def test_create_set():
    assert functions.create_set([1, 2, 3, 4]) == {1, 2, 3, 4}
    assert functions.create_set([1, 2, 3, 3, 2, 4]) == {1, 2, 3, 4}
    assert functions.create_set(['a', 'b']) == {'a', 'b'}
    assert functions.create_set({'a': 1, 'b': 2, 'c': 3}) == {'a', 'b', 'c'}


def test_get_union():
    set1 = {'Paris', 'London'}
    set2 = {'Moscow', 'Paris'}
    result = {'London', 'Moscow', 'Paris'}
    assert functions.get_union(set1, set2) == result


def test_get_intersection_of_many():
    set1 = {'Paris', 'London'}
    set2 = {'Moscow', 'Paris'}
    result = {'Paris'}
    assert functions.get_intersection_of_many(set1, set2) == result



# def test_generate_diff():
#     file1 = 'file1.json'
#     file2 = 'file2.json'
#     result = '''{
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }'''
#     assert functions.generate_diff(file1, file2) == result

