from calibration.flats import FlatCombined, Flat
from utils.test import test_file
from utils.image import ArrayImage
from settings import ORDERS
# import numpy as np


class FlatTest:
    def __init__(self, test_filename):
        self.flat1 = Flat(test_filename)
        self.flat2 = Flat(test_filename)
        self.fcomb = FlatCombined([self.flat1, self.flat2], ORDERS)

    def test_combination(self):
        return FlatCombined([self.flat1, self.flat2], True).image

    def test_canny(self):
        # return Spline(self.test_spline()).canny()
        return self.fcomb.canny()

    def test_edges(self):
        return self.test_canny().edges

    def test_fill(self, seed_point):
        return self.test_canny().fill(seed_point)

    def test_locate(self):
        return self.fcomb.locate_orders()


fill_seed = (200, 70)
test = FlatTest(test_file)
# test.fcomb.show()
# ArrayImage(test.fcomb.canny().edges).show()
# print('canny')
# ArrayImage(test.test_fill(fill_seed)).show()
# test.test_canny().show_edges_overlay()
# test.test_canny().show_fill_overlay(fill_seed)
test.test_locate().show_all_fill_overlay()
# test.test_canny()
