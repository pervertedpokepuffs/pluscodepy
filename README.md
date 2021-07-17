# pluscodepy
Simple plus code to lat/long decoder written for White Flag Project.

## Quickstart
1. `pip install pluscodepy`
2. `list_of_places = [{'name': 'Some place string', 'latitude': 1.921313, 'longitude': 207.124523}, ...]`
3. `converter = pluscodepy.Converter(filestream)`
4. `latitude, longitude = converter.decode('GM83+2X Skudai, Johor')`

## Install
`pip install pluscodepy`
## Usage
### Parameters
#### \_\_init\_\_(index: list[dict])
`index: list[dict]` List of dictionaries with a name field for the place string, a longitude field, and a latitude field.

#### decode(pluscode: str)
`pluscode: str` Plus code to be decoded.

Return

`Union[(float, float), False]`
Returns a float of tuples representing latitude and longitude OR returns false if the pluscode cannot be decoded.

#### getCities()
Return

`list[dict]` List of dictionaries with a name field for the place string, a longitude field, and a latitude field.


## How it works
The converter makes use of the [Google Open Location Code](https://github.com/google/open-location-code/tree/main/python) library to decode and works with both full code and short code. The converter will try to work offline whenever possible.

If the input is a full code, it will just decode without any preprocessing. If a place string is detected in the code, it'll first check for the place's lat/long in the index file, and convert that to the 4 digit prefix. If the place is not yet indexed, it'll search on the [Nominatim OSM API](https://nominatim.openstreetmap.org) and index valid result's lat/long into the index file for future use. And then the lat/long values are returned as a tuple `(latitude, longitude)`.