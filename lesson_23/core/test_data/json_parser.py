import json


class JSONParser:

    @staticmethod
    def serialize_json_from_dict(data: dict[str, object]) -> json:
        return json.dumps(data)

