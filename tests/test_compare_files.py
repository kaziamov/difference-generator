from gendiff.scripts.gendiff import compare_files, open_two_files
from tests.paths import path

# def test1():
#     file1 = path + 'flat_1.json'
#     file2 = path + 'flat_2.json'
#     readed_files = open_two_files(file1, file2)
#     with open(path + 'flat_r.txt', 'r') as f:
#         result = [line.strip() for line in f.readlines()]
#     assert compare_files(readed_files) == result
#
# def test2():
#     file1 = path + 'flat_1.json'
#     file2 = path + 'flat_2.json'
#     readed_files = open_two_files(file1, file2)
#     result = open(path + 'flat_r.txt').read().strip()
#     assert compare_files(readed_files) == result