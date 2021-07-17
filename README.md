# pluscodepy
Simple plus code to lat/long decoder written for White Flag Project.

## Quickstart
1. `pip install pluscodepy`
2. `converter = pluscodepy.Converter('places.json')`
3. `latitude, longitude = converter.decode('GM83+2X Skudai, Johor')`

## Install
`pip install pluscodepy`
## Usage
### Parameters
#### \_\_init\_\_(filename: str)
`filename: str` Name/path to file the json containing a place index. If none exists, one will be created.

#### decode(pluscode: str)
`pluscode: str` Plus code to be decoded.
### Return
`Union[(float, float), False]`
Returns a float of tuples representing latitude and longitude OR returns false if the pluscode cannot be decoded.

## How it works
The converter makes use of the [Google Open Location Code](https://github.com/google/open-location-code/tree/main/python) library to decode and works with both full code and short code. The converter will try to work offline whenever possible.

If the input is a full code, it will just decode without any preprocessing. If a place string is detected in the code, it'll first check for the place's lat/long in the index file, and convert that to the 4 digit prefix. If the place is not yet indexed, it'll search on the [Nominatim OSM API](https://nominatim.openstreetmap.org) and index valid result's lat/long into the index file for future use. And then the lat/long values are returned as a tuple `(latitude, longitude)`.