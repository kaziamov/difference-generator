# Import build-in modules
import json
# Import third-party modules
import yaml


def convert_to_yml(document):
    """Input Python dictionary and convert to yalm"""
    return yaml.dump(document, default_flow_style=False)


def convert_to_json(document):
    """Input Python dictionary and convert to json"""
    return json.dumps(document,
                      skipkeys=True,
                      allow_nan=True,
                      indent=4,
                      separators=("\n", ": ")
                      )


