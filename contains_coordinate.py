import itertools
import sys
import fiona
from fiona.crs import from_epsg
from pyproj import Proj, transform
from shapely.geometry import shape,mapping, Point, Polygon, MultiPolygon
from geojson import Point, Polygon, Feature


# ref:  https://gis.stackexchange.com/questions/208546/check-if-a-point-falls-within-a-multipolygon-with-python
# Use a quad tree to store coordinates and name tree 
# find the aquifer name given an address and a dictionary of aquifers along with 
# their coordinates

def coordinate_aq_code(coordinate, path_to_shp_file):
    """
    checks to see if a given coordinate is within the polygon/multipolygon mapped
    out by a shape file

    :param coordinate: the coordinates/latitude and longtitude of the given point
    :param path_to_shp_file: path to the .shp file for the given aquifer
    :return: a boolean (whether or not the coordinate is in a given shape file)
    """ 
    if coordinate is None:
      return False
    multipol = fiona.open(path_to_aq_VA_shp)
    multi= multipol.next() # only one feature in the shapefile
    point = Feature(geometry=Point((float(coordinate[1]), float(coordinate[0])))) # create point
    # point = Feature(geometry=Point(((-81), (37)))) # create point
    # print(point)
    point = shape(point['geometry'])
    if point.within(shape(multi['geometry'])):
      print('the aquifer code is', multi['properties']['AQ_CODE'])
      return multi['properties']['AQ_CODE']
    return False 

if __name__ == '__main__':
    if (len(sys.argv) != 3):
       print("Incorrect Number Of Arguments")
    else:
        print(contains_coordinate(sys.argv[1], sys.argv[2]))
