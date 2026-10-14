import json

class JsonWrapper:
    def dumps(self, json_path, json_data):
        with open(json_path, 'w') as f:
            f.write(
                json.dumps(json_data, indent=4)
            )