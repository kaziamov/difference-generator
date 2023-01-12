# Import local modules
import gendiff.scripts.formatters.stylish as stylish


def format_tree(tree, style='stylish'):
    """Format tree with selected style"""
    options = {
        'stylish': stylish,
    }
    formatter = options[style]
    result = formatter._format_node_(tree)
    return result
