from gendiff.scripts.gendiff import generate_diff
from tests.conftest import (tree_fixtures, tree_plain_fixtures)
import pytest


@pytest.mark.parametrize("file1, file2, expected", tree_fixtures)
def test_generate_diff_tree_files(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1, file2, expected", tree_plain_fixtures)
def test_generate_diff_tree_files_in_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected
