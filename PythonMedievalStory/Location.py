

class Location:
    name = ""
    land_size = 0
    num_people = 0

    def __init__(self, name, land_size, num_people):
        self.set_name(name)
        self.set_land_size(land_size)
        self.set_num_people(num_people)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_land_size(self, land_size):
        self.land_size = land_size

    def get_land_size(self):
        return self.land_size

    def set_num_people(self, num_people):
        self.num_people = num_people

    def get_num_people(self):
        return self.num_people