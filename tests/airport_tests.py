import unittest
from mock import Mock
from nose.tools import *
from airport.airport import Airport


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()

    def test_airport_initializes_with_empty_planes_array(self):
        self.assertEqual(self.airport.planes, [])

    def test_instruct_plane_to_land(self):
        self.airport.instruct_to_land(self.plane)
        self.assertIn(self.plane, self.airport.planes)

    def test_instruct_plane_to_take_off(self):
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_take_off(self.plane)
        self.assertNotIn(self.plane, self.airport.planes)

    def test_initialize_with_capacity_equal_to_default_capacity(self):
        self.assertEqual(self.airport.capacity, 10)

    def test_to_set_max_capacity(self):
        self.airport.set_capacity(10)
        self.assertEqual(self.airport.capacity, 10)

    def test_instruct_to_land_raises_error_when_airport_is_full(self):
        # for i in range(10):
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_to_land(self.plane)
        with self.assertRaises(Exception, 'Airport is full'):
            self.airport.instruct_to_land(self.plane)
