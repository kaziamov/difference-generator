# Import local modules
import gendiff.scripts.formatters.stylish as stylish
import gendiff.scripts.formatters.plain as plain
import gendiff.scripts.formatters.jsonify as jsonify

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
