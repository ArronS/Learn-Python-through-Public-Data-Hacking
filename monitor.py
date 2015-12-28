# monitor.py
# pull down data and test candidate bus distance from office
# gmaps api: AIzaSyAh0x7uXRJa57A4FNIGHJ0g3ojJM86XKV4

import urllib
from xml.etree.ElementTree import parse
import webbrowser

candidates = ['1871', '1917']
daves_latitude = 41.98062

def distance(lat1, lat2):
    'Return distance in miles between two lats'
    return 69*abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/\
getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, daves_latitude)
            print busid, dis, 'miles'
    print '-'*10


'''
    webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?center=\
41.98062,-87.668452&zoom=11&size=600x300&maptype=roadmap\
&markers=color:blue%7Clabel:S%7Cbus1lat,bus1long\
&key=AIzaSyAh0x7uXRJa57A4FNIGHJ0g3ojJM86XKV4')

bus1lat = lat
bus1long = float(bus.findtext('lat'))
'''


# loops program once per minute

import time
while True:
    monitor()
    time.sleep(60)

