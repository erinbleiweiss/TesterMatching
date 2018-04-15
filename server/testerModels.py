import json


class Bug(object):
    def __init__(self, csv_row_items):
        self.bugId = csv_row_items[0]
        self.deviceId = csv_row_items[1]
        self.testerId = csv_row_items[2]

    def __repr__(self):
        data = {
            'bugId': self.bugId,
            'deviceId': self.deviceId,
            'testerId': self.testerId
        }
        return json.dumps(data)


class Device(object):
    def __init__(self, csv_row_items):
        self.deviceId = csv_row_items[0]
        self.description = csv_row_items[1]

    def __repr__(self):
        data = {
            'deviceId': self.deviceId,
            'description': self.description
        }
        return json.dumps(data)


class TesterDevice(object):
    def __init__(self, csv_row_items):
        self.testerid = csv_row_items[0]
        self.deviceId = csv_row_items[1]

    def __repr__(self):
        data = {
            'testerId': self.testerid,
            'deviceId': self.deviceId
        }
        return json.dumps(data)


class Tester(object):
    def __init__(self, csv_row_items):
        self.testerId = csv_row_items[0]
        self.firstName = csv_row_items[1]
        self.lastName = csv_row_items[2]
        self.country = csv_row_items[3]
        self.lastLogin = csv_row_items[4]

    def __repr__(self):
        data = {
            'testerId': self.testerId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'country': self.country,
            'lastLogin': self.lastLogin
        }
        return json.dumps(data)
