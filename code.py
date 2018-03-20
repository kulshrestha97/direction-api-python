###########################################
# CSE 3002 → Internet and Web Programming #
###########################################

__author__ = "Rajat Kulshreshtha"
from time import gmtime, strftime #Time Package
from gmplot import gmplot #Plot Google Maps
import googlemaps #Maps API Python Client
import datetime #for extracting current time for arrival
import urllib.request # As we have to do a web request
import json #Useful in getting the request in dictionary
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'Add your API here'
plt = gmplot.GoogleMapPlotter.from_geocode("Vellore")


origin = str(input("Where are you now?\n"))
destination = str(input("Where do you want to go?\n"))
origin2 = origin.replace(' ','+')
destination2 = destination.replace(' ','+')
gmaps = googlemaps.Client(api_key)
current = datetime.datetime.now()
navigation_req = 'origin={}&destination={}&key={}'.format(origin2,destination2,api_key)

request = endpoint+navigation_req
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print('\nMaking JSON.....')
directions_pp = json.dumps(directions, indent=4, sort_keys=True)
gmp = googlemaps.directions
routes = directions['routes']
f = open("map.json","w+")
f.write(directions_pp)
f.close()
html = open("map_dir.html",'w+')

print("Extracting Information")
for i in range(len(routes[0]['legs'][0]['steps'])):
    print(".")
    html.write(routes[0]['legs'][0]['steps'][i]['html_instructions'])
    html.write('<br>')

print('Extraction successfully all files!\nRun map_dir.html')
print("Distance between {} and {} is: \n".format(origin, destination))
print((routes[0]['legs'][0]['distance']['text']))

html.close()

