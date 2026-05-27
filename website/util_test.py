import base64
import json


def json_base64(obj):
    return base64.b64encode(
        json.dumps(obj, separators=(",", ":")).encode("UTF-8")
    ).decode("US-ASCII")


def test_foo():
    assert json_base64({"a": 1}) == "eyJhIjoxfQ=="
    assert base64.b64decode(json_base64({"a": 1})).decode("UTf-8") == '{"a":1}'
