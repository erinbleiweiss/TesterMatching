import csv
import os

from collections import OrderedDict
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

    def get_device_name(self, deviceId):
        for device in self.devices:
            if deviceId == device.deviceId:
                return device.description
        return "Unknown Device"

    def search(self, country_filter=None, device_filter=None):
        # If no countries or devices are provided, search all
        if not country_filter:
            country_filter = list(self.get_countries())
        if not device_filter:
            device_filter = list(self.get_devices())

        tester_ids_matching_country = [t.testerId for t in self.testers
                                       if t.country in country_filter]

        device_ids_matching_description = [d.deviceId for d in self.devices
                                           if d.description in device_filter]

        # Get bugs filtered by country, device criteria
        matching_bugs = [b for b in self.bugs if
                         b.testerId in tester_ids_matching_country and
                         b.deviceId in device_ids_matching_description]

        # Create dictionary of testers with bugs assigned to each tester
        bugs_sorted_by_tester = {}
        for bug in matching_bugs:
            bugs_sorted_by_tester.setdefault(bug.testerId, []).append(bug)

        # Create nested dictionaries sorting each tester's bug by device type
        for (tester, bugs) in bugs_sorted_by_tester.items():
            total_bugs_for_tester = len(bugs)
            bugs_sorted_by_device = {}
            for bug in bugs:
                bugs_sorted_by_device.setdefault(bug.deviceId, []).append(bug)
            for (device, bugs) in bugs_sorted_by_device.items():
                bugs_sorted_by_device[device] = len(bugs)

            # Map device ID to device name
            bug_count_by_device_name = dict((self.get_device_name(key), value)
                                            for (key, value)
                                            in bugs_sorted_by_device.items())

            # Add total bug count for each tester
            bug_count_by_device_name['Total'] = total_bugs_for_tester

            # Sort bug counts for each device in descending order
            bugs_sorted_by_tester[tester] = OrderedDict(sorted(
                    bug_count_by_device_name.items(),
                    key=lambda i: i[1],
                    reverse=True))

        # Sort testers by total bug count in descending order
        testers_sorted_by_bug_count = OrderedDict(sorted(
                bugs_sorted_by_tester.items(),
                key=lambda i: i[1]['Total'],
                reverse=True))

        return testers_sorted_by_bug_count




