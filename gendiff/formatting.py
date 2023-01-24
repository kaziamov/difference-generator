# Import local modules
import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.jsonify as jsonify

FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': jsonify,
}


def format_tree(tree, style):
    """Format tree with selected style"""
    formatter = FORMATS[style]
    result = formatter._format_node_(tree)
    return result


def get_formats():
    return FORMATS.keys()
