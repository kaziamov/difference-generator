# from gendiff.functions import convert, functions
#
#
# def test_convert_to_json():
#     path_ = 'tests/fixtures/test_convert_files/1/'
#     path_file1 = path_ + "file1.json"
#     result_file = path_ + "result.txt"
#
#     data = functions.open_file(path_file1)
#
#     with open(result_file, "r") as file:
#         result = file.read()
#     assert convert.convert_to_yml(data) == result
#
#
# def test_convert_to_yaml():
#     path_ = 'tests/fixtures/test_convert_files/2/'
#     path_file1 = path_ + "file1.yaml"
#     result_file = path_ + "result.txt"
#
#     data = functions.open_file(path_file1)
#
#     with open(result_file, "r") as file:
#         result = file.read()
#     assert convert.convert_to_json(data) == result
#
#
# def test_convert_to_yaml2():
#     path_ = 'tests/fixtures/test_convert_files/3/'
#     path_file1 = path_ + "file1.yml"
#     result_file = path_ + "result.txt"
#
#     data = functions.open_file(path_file1)
#
#     with open(result_file, "r") as file:
#         result = file.read()
#     assert convert.convert_to_json(data) == result
