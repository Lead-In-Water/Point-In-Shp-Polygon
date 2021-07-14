################################################################################
#################################local testing##################################
################################################################################

from contains_address import *
path_to_aq_VA_shp = "shp files/aq_VA.shp"
#  test
address_one = "337 North 40th Street,Philadelphia, PA, 19104" #not in VA_AQ
address_two = "2222 Max Meadows, Virginia"  #in VA_AQ
address_three = "Honaker, Virginia" #in VA_AQ
address_four = "119 Hillman Dr, Honaker, VA 24260" #in VA_AQ
address_five = "1135 Carthage St, Sanford, NC 27330"  #not in VA_AQ
address_six = "11221 New Garden Rd, Honaker, VA 24260"  # in VA_AQ
address_seven = "10300 New Garden Rd, Honaker, VA 24260"  # in VA_AQ


print("address one coords: " + str(address_coordinates(address_one)))
print(contains_address(address_one, path_to_aq_VA_shp))
assert(contains_address(address_one, str(path_to_aq_VA_shp)) == False)
print("address two coords: " + str(address_coordinates(address_two)))
print(contains_address(address_two, str(path_to_aq_VA_shp)))
assert(contains_address(address_two, str(path_to_aq_VA_shp)) != False)
print("address three coords: " + str(address_coordinates(address_three)))
print(contains_address(address_three, str(path_to_aq_VA_shp)))
assert(contains_address(address_three, str(path_to_aq_VA_shp)) != False)
print("address four coords: " + str(address_coordinates(address_four)))
print(contains_address(address_four, str(path_to_aq_VA_shp)))
assert(contains_address(address_four, str(path_to_aq_VA_shp)) != False)
print("address five coords: " + str(address_coordinates(address_five)))
print(contains_address(address_five, str(path_to_aq_VA_shp)))
assert(contains_address(address_five, str(path_to_aq_VA_shp)) == False)
print("address six coords: " + str(address_coordinates(address_six)))
print(contains_address(address_six, str(path_to_aq_VA_shp)))
assert(contains_address(address_six, str(path_to_aq_VA_shp)) != False)
print("address seven coords: " + str(address_coordinates(address_seven)))
print(contains_address(address_seven, str(path_to_aq_VA_shp)))
assert(contains_address(address_seven, str(path_to_aq_VA_shp)) != False)