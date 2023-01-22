from gendiff.receiving import get_format
import pytest


@pytest.mark.parametrize("input_value, expected", [
                        ('file.txt', 'txt'),
                        ('file.json', 'json'),
                        ('file.yaml', 'yaml')])
def test_file_format(input_value, expected):
    assert get_format(input_value) == expected
