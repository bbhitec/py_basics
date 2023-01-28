#
# [mst] web_html_json.py
# working with web data
# based on the lynda.com 'Learning Python' course (chapter 5)
#
# log:
# - 2020.12 initial
# - html communication, code checking and reading data
# - working with json as a dict. used geo earthquake data
#


#import urllib2  # used in py2, slightly different interface
import urllib.request
import json     # working with Java Script Object Notation


def printResult(data):

    # Use the json module to load the string data into a dictionary (hash table)
    json_data = json.loads(data)

    # this way we can operate a json just like any other python object
    # the json fields are listed here: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    if "title" in json_data["metadata"]:
        print (json_data["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    print (str(json_data["metadata"]["count"]) + " events recorded")

    # for each event, print the conditional data
    print ("of which, the following were over 4.5 in magnitude and were reported felt")
    for evt in json_data["features"]:
        mag = evt["properties"]["mag"]
        felt = evt["properties"]["felt"]
        place = evt["properties"]["place"]
        if (mag >= 4.0 and felt != None and felt > 0):
            print ("%2.1f" % mag, place.encode("utf-8"), ", reported " + str(felt) + " times")  # [demo] point to a specific encoding (international data)


def main():
    #######
    # communicating with an URL. proper stages follow
    url = "http://joemarini.com"
    print ("----- communicating with an url: " + url)

    # REQUEST to open a connection
    request_open = urllib.request.urlopen("http://joemarini.com")

    # CODE CHECK
    # html ok code is '200'. more: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    print ("result code: " + str(request_open.getcode()))   # cast code to string

    # READ DATA
    data = request_open.read().decode("utf-8") # decode the data as UTF-8
    print ("printing data...")
    print (data)



    #######
    # working with JSON: geodata for earthquakes with a higher magnitute than 2.5
    url_geo = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    print ("----- requesting a json from:" + url_geo)

    # open url and read the data
    req_open_geo = urllib.request.urlopen(url_geo)
    if req_open_geo.getcode() == 200:
        # only read on an ok code
        data_geo = req_open_geo.read()
        printResult(data_geo)
    else:
        print ("error: can't read url!!! error code: "  + str(req_open_geo.getcode()))


if __name__ == "__main__":
    main()
