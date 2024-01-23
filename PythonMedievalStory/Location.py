"""
@author abbybrown
@date 01/20/24
@filename Location.py

Generates the locations where each activity may occur.
"""


class Location:
    name = ""
    land_size = 0
    num_people = 0

    # constructor
    def __init__(self, name, land_size, num_people):
        self.set_name(name)
        self.set_land_size(land_size)
        self.set_num_people(num_people)

    # sets the name for the location
    def set_name(self, name):
        self.name = name

    # gets the name for the location
    def get_name(self):
        return self.name

    # sets the land size for the location
    def set_land_size(self, land_size):
        self.land_size = land_size

    # gets the land size for the location
    def get_land_size(self):
        return self.land_size

    # sets the number of people in a location
    def set_num_people(self, num_people):
        self.num_people = num_people

    # gets the number of people in a location
    def get_num_people(self):
        return self.num_people
