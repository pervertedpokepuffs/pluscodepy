import json
import re
import openlocationcode.openlocationcode as olc

class Converter:
    def __init__(self, cities_file):
        self.cities = json.load(cities_file)

    def decode(self, pluscode):
        match = re.match('^(\S*\S{2})\s*(.*?),\s*(.*)$', pluscode)
        if match is not None:
            if len(match.groups()) > 1:
                fullcode = self.convertShortcodeToFull(match.group(1), match.group(2))
        else:
            fullcode = pluscode
        if not fullcode:
            return False
        try:
            decoded = olc.decode(fullcode)
        except:
            return False
        return (decoded.latitudeCenter, decoded.longitudeCenter)

    def convertShortcodeToFull(self, pluscode, city):
        city = [item for item in self.cities if item['name'] == city]
        if len(city) == 0:
            return False
        city = city.pop()
        city_prefix = olc.encode(city['latitude'], city['longitude'])[0:4]
        return f'{city_prefix}{pluscode}'