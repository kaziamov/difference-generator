from gendiff.scripts.parsing import load_json, load_yaml
from tests.conftest import fixtures_path
import pytest


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.json'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_json(input_value, expected):
    assert load_json(input_value) == expected


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.yaml'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_yaml(input_value, expected):
    assert load_yaml(input_value) == expected


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.yml'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_yml(input_value, expected):
    assert load_yaml(input_value) == expected
