from gendiff.parsing import parse_json, parse_yaml, parse_data
from gendiff.receiving import get_data

from tests.conftest import fixtures_path

import pytest
import requests


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.json'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_json(input_value, expected):
    assert parse_json(get_data(input_value)) == expected


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.yaml'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_yaml(input_value, expected):
    assert parse_yaml(get_data(input_value)) == expected


@pytest.mark.parametrize("input_value, expected", [
    (fixtures_path('flat/')('flat_1.yml'), {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False})
])
def test_parse_yml(input_value, expected):
    assert parse_yaml(get_data(input_value)) == expected


def test_parse_from_get_request():
    json_data = requests.get('https://dummyjson.com/products/1').text
    parsed_data = parse_data(json_data, 'json')
    assert parsed_data == {'id': 1, 'title': 'iPhone 9', 'description': 'An apple mobile which is nothing like apple', 'price': 549, 'discountPercentage': 12.96, 'rating': 4.69, 'stock': 94, 'brand': 'Apple', 'category': 'smartphones', 'thumbnail': 'https://i.dummyjson.com/data/products/1/thumbnail.jpg', 'images': ['https://i.dummyjson.com/data/products/1/1.jpg', 'https://i.dummyjson.com/data/products/1/2.jpg', 'https://i.dummyjson.com/data/products/1/3.jpg', 'https://i.dummyjson.com/data/products/1/4.jpg', 'https://i.dummyjson.com/data/products/1/thumbnail.jpg']}
