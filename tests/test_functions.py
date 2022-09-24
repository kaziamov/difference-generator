from gendiff.functions import functions
import pytest
from tests.fixtures._paths import _PATH


def test_open_file1():
    assert open(_PATH + 'open1.json')


def test_open_file2():
    with pytest.raises(Exception) as exc:
        open('not_exist.fantasy')
    assert 'No such file or directory' in str(exc)


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


# def test_gendiff1():
#     assert functions.generate_diff(_PATH + 'gendiff1_file1.json', _PATH + 'gendiff1_file2.json') == open(_PATH + 'gendiff1_result.txt', "r").read().strip()
#
#
# def test_gendiff2():
#     assert functions.generate_diff(_PATH + 'gendiff2_file1.yaml', _PATH + 'gendiff2_file2.yaml') == open(_PATH + 'gendiff2_result.txt', "r").read().strip()
#
#
# def test_gendiff3():
#     assert functions.generate_diff(_PATH + 'gendiff3_file1.yml', _PATH + 'gendiff3_file2.yml') == open(_PATH + 'gendiff3_result.txt', "r").read().strip()
