from gendiff.scripts import gendiff


def generate_diff(file1, file2, format="stylish"):
    return gendiff.generate_diff(file1, file2, format)
