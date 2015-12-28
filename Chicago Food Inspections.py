# Chicago Food Inspections
# Pie Chart Showing the Outcomes fo Chicago food safety inspections


import csv
from collections import Counter

f = open('food.csv', 'r')
food = list(csv.DictReader(f))

total_count = len(food) # Total number of inspections within database


print total_count

outcomes = Counter()


for restaurant in csv.DictReader(f):
    result = row['Results']
    outcomes[result] += 1

print sum(outcomes.values())
