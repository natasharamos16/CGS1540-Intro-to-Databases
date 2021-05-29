"""
    You may use the naive approach or an approach that uses list comprehensions.
    It is also up to you whether to use functions, although, if you
    are using list comprehensions, you will likely need function(s) that
    return values.
"""
# You are not required to use pprint,
# but is is handy to have for testing
from pprint import pprint
import csv
from operator import itemgetter  # for extra credit part

# put your code here
import csv

with open('places.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    row = list(csv_reader)
    pprint(row)

str = 'Pizza hut'
print(str.title())

str = 'trulieve tampa'
print(str.title())

str = 'BOBACUP'
print(str.title())

str = 'cigar city brewery'
print(str.title())

str = '(swah-rey)'
print(str.title())

str = '(swah-rey)'
print(str.title())

list = '2550 E Fowler Ave, Tampa, FL 33612'
print(list.split(','))

list = '8701 N Dale Mabry Hwy, Tampa, FL 33614'
print(list.split(','))

list = '24546 US Highway 19 N, Clearwater, FL 33763'
print(list.split(','))

list = '2732 E Fowler Ave, Tampa, FL 33612'
print(list.split(','))

list = '3345 Caverns Rd, Marianna, FL 32446'
print(list.split(','))

list = '2300-2398 W Horatio St, Tampa, FL 33609'
print(list.split(','))

list = '3924 W Spruce St, Tampa, FL 33607'
print(list.split(','))

list = '11706 N 51st St, Tampa, FL 33617'
print(list.split(','))

list = '10001 N. McKinley Drive, Tampa, FL 33612'
print(list.split(','))

list = '5880 E Fowler Ave, Tampa, FL 33617'
print(list.split(','))

list = '10053 N Dale Mabry Hwy, Tampa, FL 33618'
print(list.split(','))

list = '10165 McKinley Dr, Tampa, FL 33612'
print(list.split(','))

list = '1 Causeway Blvd, Clearwater, FL 33767'
print(list.split(','))

list = '2105 Central Ave, St. Petersburg, FL 33713'
print(list.split(','))

list = '1101 W Sligh Ave., Tampa, FL 33604'
print(list.split(','))

string ='Food, pizzeria, fast food, late night, casual, comfort'
print(string.lower())

string = 'Outdoor, Hiking, Park'
print(string.lower())

string = 'Tacos, Mexican Grill, Burritos'
print(string.lower())

string = 'Water park, Restaurants'
print(string.lower())

string = 'Park, Beach, Scenery'
print(string.lower())

string = 'Zoo, Animals, Wildlife'
print(string.lower())















