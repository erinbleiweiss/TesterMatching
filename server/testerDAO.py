import csv
import os
from testerModels import Bug, Device, TesterDevice, Tester


class TesterDAO:

    def __init__(self):
        current_folder = os.path.dirname(os.path.realpath(__file__))
        self.csv_source_path = os.path.join(current_folder, 'csv')

        self.bugs = self.parse_data('bugs.csv', Bug)
        self.devices = self.parse_data('devices.csv', Device)
        self.tester_devices = self.parse_data('tester_device.csv', TesterDevice)
        self.testers = self.parse_data('testers.csv', Tester)

    def parse_data(self, file_name, model_type):
        file = os.path.join(self.csv_source_path, file_name)
        data = []
        with open(file, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            for (idx, row) in enumerate(reader):
                # Ignore CSV headers
                if idx > 0:
                    data.append(model_type(row))
        return data

    def get_countries(self):
        countries = []
        for tester in self.testers:
            if tester.country not in countries:
                countries.append(tester.country)
        return countries

    def get_devices(self):
        devices = []
        for device in self.devices:
            if device.description not in devices:
                devices.append(device.description)
        return devices

