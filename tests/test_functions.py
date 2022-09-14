from gendiff.functions import functions


def test_convert_to_set():
    assert functions.convert_to_set([1, 2, 3, 4]) == {1, 2, 3, 4}
    assert functions.convert_to_set([1, 2, 3, 3, 2, 4]) == {1, 2, 3, 4}
    assert functions.convert_to_set(['a', 'b']) == {'a', 'b'}
    assert functions.convert_to_set({'a': 1, 'b': 2, 'c': 3}) == {'a', 'b', 'c'}


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


def test_get_unique_in_set1():
    set1 = {'Paris', 'London'}
    set2 = {'Moscow', 'Paris'}
    result = {'London'}
    assert functions.get_unique_in_set1(set1, set2) == result


def test_get_unique_in_set2():
    set1 = {'Paris', 'London'}
    set2 = {'Moscow', 'Paris'}
    result = {'Moscow'}
    assert functions.get_unique_in_set2(set1, set2) == result


def test_generate_diff():
    path_ = 'tests/fixtures/test_gen_diff/1/'
    path_file1 = path_ + "file1.json"
    path_file2 = path_ + "file2.json"
    result_file = path_ + "result.txt"
    with open(result_file, "r") as file:
        result = file.read()
    assert functions.generate_diff(path_file1, path_file2) == print(result)

# def test_generate_diff2():
#     path_file1 = "tests/fixtures/test_gen_diff/file1.yaml"
#     path_file2 = "tests/fixtures/test_gen_diff/file2.yml"
#     result_file = "tests/fixtures/test_gen_diff/file2.txt"
#     result = ''''''
#     assert functions.generate_diff(path_file1, path_file2) == print(result)
