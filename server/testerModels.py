class Bug(object):
    def __init__(self, csv_row_items):
        self.bugId = csv_row_items[0]
        self.deviceId = csv_row_items[1]
        self.testerId = csv_row_items[2]


class Device(object):
    def __init__(self, csv_row_items):
        self.deviceId = csv_row_items[0]
        self.description = csv_row_items[1]


class TesterDevice(object):
    def __init__(self, csv_row_items):
        self.testerid = csv_row_items[0]
        self.deviceId = csv_row_items[1]


class Tester(object):
    def __init__(self, csv_row_items):
        self.testerId = csv_row_items[0]
        self.firstName = csv_row_items[1]
        self.lastName = csv_row_items[2]
        self.country = csv_row_items[3]
        self.lastLogin = csv_row_items[4]

