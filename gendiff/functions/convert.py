# Import build-in modules
import json
import yaml


def convert_to_yml(document):
    """Input Python dictionary and convert to yalm"""
    return yaml.dump(document)


def convert_to_json(document):
    """Input Python dictionary and convert to json"""
    return json.dumps(document)


