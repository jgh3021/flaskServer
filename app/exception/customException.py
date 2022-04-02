import json

class InvalidAPIUsage(Exception):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        else:
            self.status_code = 400
        self.payload = payload

    def to_dict(self):
        rv = json.dumps({
            "code":  self.status_code,
            "message": self.message
        })
        return rv