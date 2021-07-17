# pluscodepy
Simple plus code to lat/long decoder written for White Flag Project.

## Install
`pip install pluscodepy`

## Usage
```py
import pluscodepy

# The package works completely offline so it will require a a list of cities in
# JSON format, containing at least the city name and its latitude and longitude
# coordinates. Example of a valid JSON file would be:
# [{
#   "name": city,
#   "latitude": 1.921312,
#   "longitude": 213.123123
# },
# ...
# ]
with open('cities.json', 'r', encoding='utf-8') as json_file:
    converter = pluscodepy.Converter(json_file)

# Outputs a tuple containing the lat/long. In this example it is (1.5150625, 103.6549375). If it fails to decode it'll output false.
print(converter.decode('GM83+2X Skudai, Johor'))
```
You can get city data from http://download.geonames.org/export/dump/ and downloading the dump of the country you are decoding against. Just make sure to convert it into a valid JSON before feeding it into the constructor.