from gendiff.scripts import gendiff


def main(file1, file2):
    return gendiff.generate_diff(file1, file2)
