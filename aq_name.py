import sys
# Get the aquifer name from the 
def aq_name(path_to_shp_file):
    """
    Computes the name of a given aquifer given it's shape file 

    :param path_to_shp_file: path to the .shp file for the given aquifer
    :return: a string (name of the aquifer)
    """ 
    str_ags = path_to_shp_file.split('/')
    str_aq = ""
    if len(str_ags) >= 2:
        str_aq = str(str_ags[1])
    print(str_aq)
    return str_aq   



if __name__ == '__main__':
    aq_name(sys.argv[1])
