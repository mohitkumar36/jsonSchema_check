from jsonschema import Draft7Validator
from json import load


def validate_schema(json_File, schema_File):
    validator = Draft7Validator(schema_File)
    tmp = list(validator.iter_errors(json_File))
    if not tmp:
        print(True)
    else:
        print(False)


with open("schema.json") as f:
    schema = load(f)

with open('data.json') as json_file:
    data = load(json_file)

validate_schema(data["data1"], schema)