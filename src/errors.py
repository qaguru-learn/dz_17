class WrongStatusCode(Exception):

    def __init__(self, code, expected):
        super().__init__(f"StatusCode - '{code}' but {expected} expected")


class WrongJson(Exception):

    def __init__(self, json, expected_json):
        super().__init__(f"Json - '{json}' but {expected_json} expected")
