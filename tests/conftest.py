import os
import pytest
import json

def fixtures_path(path):
    return os.path.join(os.path.dirname(__file__), 'fixtures/', path, '{}').format


flat_dir = fixtures_path('flat/')


flat_expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

flat_fixtures = [
    (flat_dir('flat_1.json'), flat_dir('flat_2.yaml'), flat_expected
     ),
]

tree_fixtures = flat_fixtures
