#!/bin/python

# Chapter 13 - Python for Informatics


import urllib
# imports the json library
import json


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    # Builds the url from the peaces we want to query
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    # print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    # print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # print json.dumps(js, indent=4)


    i = len(js["results"][0]["address_components"]) - 1
    country = js["results"][0]["address_components"][i]["short_name"]

    print country

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print 'lat',lat,'lng',lng
    # location = js['results'][0]['formatted_address']
    # print location
