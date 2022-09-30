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


# ('{\n'\n 'common: {\n'\n '+ follow: false\n'\n '    setting1: Value 1\n'\n '  - setting2: 200\n'\n '  - setting3: true\n'\n '  + setting3: null\n'\n '  + setting4: blah blah\n'\n '  + setting5: {\n'\n 'key5: value5\n'\n '}\n'\n '    setting6: {\n'\n 'doge: {\n'\n '- wow: \n'\n '  + wow: so much\n'\n '}\n'\n '    key: value\n'\n '  + ops: vops\n'\n '}\n'\n '}\n'\n '    group1: {\n'\n '- baz: bas\n'\n '  + baz: bars\n'\n '    foo: bar\n'\n '  - nest: {\n'\n 'key: value\n'\n '}\n'\n '  + nest: str\n'\n '}\n'\n '  - group2: {\n'\n 'abc: 12345\n'\n '  deep: {\n'\n 'id: 45\n'\n '}\n'\n '}\n'\n '  + group3: {\n'\n 'deep: {\n'\n 'id: {\n'\n 'number: 45\n'\n '}\n'\n '}\n'\n '  fee: 100500\n'\n '}\n'\n '}')
# ('{\n'\n '    common: {\n'\n '      + follow: false\n'\n '        setting1: Value 1\n'\n '      - setting2: 200\n'\n '      - setting3: true\n'\n '      + setting3: null\n'\n '      + setting4: blah blah\n'\n '      + setting5: {\n'\n '            key5: value5\n'\n '        }\n'\n '        setting6: {\n'\n '            doge: {\n'\n '              - wow:\n'\n '              + wow: so much\n'\n '            }\n'\n '            key: value\n'\n '          + ops: vops\n'\n '        }\n'\n '    }\n'\n '    group1: {\n'\n '      - baz: bas\n'\n '      + baz: bars\n'\n '        foo: bar\n'\n '      - nest: {\n'\n '            key: value\n'\n '        }\n'\n '      + nest: str\n'\n '    }\n'\n '  - group2: {\n'\n '        abc: 12345\n'\n '        deep: {\n'\n '            id: 45\n'\n '        }\n'\n '    }\n'\n '  + group3: {\n'\n '        deep: {\n'\n '            id: {\n'\n '                number: 45\n'\n '            }\n'\n '        }\n'\n '        fee: 100500\n'\n '    }\n'\n '}')