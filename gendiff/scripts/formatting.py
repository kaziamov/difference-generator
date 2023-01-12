# Import local modules
import gendiff.scripts.formatters.stylish as stylish
import gendiff.scripts.formatters.plain as plain


def format_tree(tree, style):
    """Format tree with selected style"""
    options = {
        'stylish': stylish,
        'plain': plain,
    }
    formatter = options[style]
    result = formatter._format_node_(tree)
    return result
