# Chicago Pothole Finder

import csv
import operator

def make_block(address):
    # Reduce addresses down
    parts = address.split(' ')
    num = parts[0]  # Selects first word from list, alt: num[0][:-2] below
    parts[0] = num[:-3] + 'XX'  # Only takes away last three, no matter length
    return ' '.join(parts)


potholes_by_block = {}

f = open('potholes.csv')

# Searches through csv file for Open potholes, adds to running dict
for row in csv.DictReader(f):

    status = row['STATUS']

    if status == 'Open':
        address = row['STREET ADDRESS']
        num_potholes = row['NUMBER OF POTHOLES FILLED ON BLOCK']
        block = make_block(address)
    
        if block not in potholes_by_block:
            # First occurance of a given address
            # Maximum of 1 pothole per Open issue
            potholes_by_block[block] = 1
        else:
            potholes_by_block[block] += 1

# Sorts dict by key and selects 10 largest
sorted_blocks = sorted(potholes_by_block.items(), key=operator.itemgetter(1))
for key, value in sorted_blocks[-10:]:
    print key, value
