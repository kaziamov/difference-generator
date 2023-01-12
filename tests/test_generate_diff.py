from gendiff.scripts.generate_diff import generate_diff
from tests.conftest import tree_fixtures, flat_fixtures, tree_plain_fixtures, flat_plain_fixtures
import pytest


@pytest.mark.parametrize("file1, file2, expected", flat_fixtures)
def test_generate_diff_flat_files(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1, file2, expected", tree_fixtures)
def test_generate_diff_tree_files(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1, file2, expected", flat_plain_fixtures)
def test_generate_diff_flat_files_in_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected


@pytest.mark.parametrize("file1, file2, expected", tree_plain_fixtures)
def test_generate_diff_tree_files_in_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected
