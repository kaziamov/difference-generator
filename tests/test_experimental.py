import json

test_data = '''{
      "name": "Wyoming",
      "abbreviation": "WY"
    }'''

def test1():
    result = {'name': 'Wyoming', 'abbreviation': 'WY'}
    assert json.loads(test_data) == result
   
    
def test2():
    result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    with open('tests/fixtures/open_read1.json', 'r') as f:
        data = f.read()
    assert json.loads(data) == result
