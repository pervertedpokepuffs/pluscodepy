import json
import re
import requests
import datetime
import time
import openlocationcode.openlocationcode as olc

class Converter:
    def __init__(self, filename):
        self.filename = filename
        self.ratelimit = 1
        with open(self.filename, 'r+', encoding='utf-8') as file:
            try:
                self.cities = json.load(file)
            except json.JSONDecodeError:
                self.cities = []
        self.lastcall = datetime.datetime.now()

    def decode(self, pluscode: str):
        match = re.match('^(\S*\+\S{2})\s*(.*?)$', pluscode)
        fullcode = None
        if match is not None:
            if match.group(2) != "":
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

    def convertShortcodeToFull(self, pluscode, place):
        city = [item for item in self.cities if item['name'] == place]
        if len(city) == 0:
            time_diff = datetime.datetime.now() - self.lastcall
            time_diff = time_diff.total_seconds()
            time_diff = self.ratelimit-time_diff
            time.sleep(time_diff if time_diff > 0 else 0)
            city = self.getNewData(place)
            if city is False: return False
            print(f'getting for {place}')
            self.cities = self.cities + [city]
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.cities, file)
        else:
            city = city.pop()
        city_prefix = olc.encode(city['latitude'], city['longitude'])[0:4]
        return f'{city_prefix}{pluscode}'

    def getNewData(self, place):
        if place == "": return False
        city = requests.get('https://nominatim.openstreetmap.org/search', params={
                'q': place,
                'format': 'json'
            })
        self.lastcall = datetime.datetime.now()
        city = city.json().pop(0)
        return {'name': place, 'latitude': float(city['lat']), 'longitude': float(city['lon'])}