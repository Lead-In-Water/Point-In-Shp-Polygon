# Import necessary libraries 
import os
import itertools
import sys
# from uszipcode import SearchEngine
import urllib.parse
import requests
from contains_coordinate import contains_coordinate 



def address_coordinates(address):

    """
    Computes the long and lat of a given address 

    :param zipcode: the zipcode of the address
    :return: a string (name of the county) or None
    """ 
    # get url for address
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    lat_long_tup = None
    if len(response) == 0:
      print('Address is not recognize')
    else:
      lat_long_tup = (response[0]["lat"],response[0]["lon"])
        # print(lat_long_tup)
    return lat_long_tup




def contains_address(address, path_to_shp_file):
    """
    checks to see if a given address is within the polygon/multipolygon mapped
    out by a shape file

    :param address: the address of the given point
    :param path_to_shp_file: path to the .shp file for the given aquifer
    :return: a boolean (whether or not the address is in a given shape file)
    """ 

    coordinate = address_coordinates(address)
    # TODO: Error checking on the coordinate (it can be none type)
    return contains_coordinate(coordinate, path_to_shp_file)



if __name__ == '__main__':
    contains_address(sys.argv[1], sys.argv[2])
