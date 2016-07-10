class Airport(object):

    DEFAULT_CAPACITY = 10

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.planes = []
        self.capacity = capacity


    def instruct_to_land(self, plane):
        self.planes.append(plane)

    def instruct_to_take_off(self, plane):
        self.planes.remove(plane)

    def set_capacity(self, value):
        self.capacity = value
