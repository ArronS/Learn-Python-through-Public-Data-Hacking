# The Travelling Suitcase
# 28.12.15

# Find busses heading north of office location

daves_latitude = 41.98062
daves_longitude = -87.668452

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat > daves_latitude:
        direction = bus.findtext('d')
        if direction.startswith('North'):
            busid = bus.findtext('id')
            print busid, lat
                       
    
