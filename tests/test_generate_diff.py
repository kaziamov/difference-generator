from gendiff.scripts.generate_diff import generate_diff
from tests.conftest import (tree_fixtures,
                            flat_fixtures,
                            tree_plain_fixtures,
                            flat_plain_fixtures,
                            flat_json_fixtures,
                            tree_json_fixtures)
import pytest



# STYLISH

@pytest.mark.parametrize("file1, file2, expected", flat_fixtures)
def test_generate_diff_flat_files(file1, file2, expected):
    assert generate_diff(file1, file2) == expected

@pytest.mark.parametrize("file1, file2, expected", tree_fixtures)
def test_generate_diff_tree_files(file1, file2, expected):
    assert generate_diff(file1, file2) == expected



# PLAIN

@pytest.mark.parametrize("file1, file2, expected", flat_plain_fixtures)
def test_generate_diff_flat_files_in_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected

@pytest.mark.parametrize("file1, file2, expected", tree_plain_fixtures)
def test_generate_diff_tree_files_in_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected



# JSON

@pytest.mark.parametrize("file1, file2, expected", flat_json_fixtures)
def test_generate_diff_flat_files_in_json(file1, file2, expected):
    assert generate_diff(file1, file2, 'json') == expected

# @pytest.mark.parametrize("file1, file2, expected", tree_json_fixtures)
# def test_generate_diff_tree_files_in_json(file1, file2, expected):
#     assert generate_diff(file1, file2, 'json') == expected