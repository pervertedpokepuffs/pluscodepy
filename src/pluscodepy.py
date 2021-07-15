import json
import re
import openlocationcode.openlocationcode as olc

class Converter:
    def __init__(self, cities_file):
        self.cities = json.load(cities_file)

    def decode(self, pluscode):
        match = re.match('(\S*)\s+?(\S*),\s*?(\S*)', pluscode)
        if len(match.groups()) > 1:
            fullcode = self.convertShortcodeToFull(match.group(1), match.group(2))
        else:
            fullcode = pluscode
        decoded = olc.decode(fullcode)
        return (decoded.latitudeCenter, decoded.longitudeCenter)

    def convertShortcodeToFull(self, pluscode, city):
        city = [item for item in self.cities if item['name'] == city].pop()
        city_prefix = olc.encode(city['latitude'], city['longitude'])[0:4]
        return f'{city_prefix}{pluscode}'