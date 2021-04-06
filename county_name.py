# Import necessary libraries 
import os
import sys
from uszipcode import SearchEngine

# TODO: Add to database
# To be store in a database with an endpoint to add
county_list = ['Montgomery','Loudoun','Albemarle','Prince William','Roanoke','Frederick','Spotsylvania','Warren',
               'Franklin','Goochland','Hanover','Carroll','Rockingham','Bedford','Pulaski','Nelson','Shenandoah',
               'Botetourt','Halifax','Floyd','Page','Rockbridge','Accomack','Northampton','Powhatan','Grayson',
               'Amelia','Louisa','Clarke','Northumberland','Giles','Stafford','Fauquier','Buckingham','Nottoway',
               'Wythe','Campbell','Prince George','Fairfax','Chesapeake','Mecklenburg','Culpeper','Madison','Augusta',
               'Rappahannock','Caroline','Orange','Westmoreland','Lunenburg','King George','Amherst','Fluvanna','Greene',
               'Craig','Virginia Beach','Charlotte','Lancaster','Pittsylvania','Essex','Henry','Appomattox','Isle of Wight',
               'King William','New Kent','Gloucester','Chesterfield','Suffolk','Dinwiddie','Lee','Bland','Russell',
               'Charles City','Highland','Patrick','Surry','Henrico','Prince Edward','Richmond County',
               'Southampton','Cumberland','Middlesex','Bath','Tazewell','Alleghany','Mathews','Smyth',
               'King & Queen','Sussex','Brunswick','Greensville','Scott','Dickenson','Wise',
               'James City','Lynchburg City','Buchanan','York','Petersburg','Richmond City','KY-Floyd']


def county_name(zipcode):
    """
    Computes the name of a county given it's zipcode 

    :param zipcode: the zipcode of the address
    :return: a string (name of the county) or None
    """ 
    search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
    zipcode_query = search.by_zipcode(str(zipcode))
    zipcode_query_dict = zipcode_query.to_dict()
    county = zipcode_query_dict['county']
    if county is None:
        print('Invalid County')
    else :
        if 'County' in county:
            county = county[:-7]
        if county in county_list:
            print('County is County List')
            print(county)
    return county



if __name__ == '__main__':
    if (len(sys.argv) != 2):
       print("Incorrect Number Of Arguments")
    else:
        county_name(sys.argv[1])

