from .flats import CombinedFlat, Flat
from pyspextool.utils.test import test_file_flat, test_file_dir
from pyspextool.utils.image import ArrayImage
from pyspextool.settings import ORDERS_RIMAS as ORDERS
import os
import numpy as np
# import numpy as np


class FlatTest:
    def __init__(self, test_filename):
        self.flat1 = Flat(test_filename)
        self.flat2 = Flat(test_filename)
        self.flat_files_dir = os.path.join(test_file_dir, 'flats', 'HK')
        self.flat_files = os.listdir(self.flat_files_dir)
        self.flats = [Flat(os.path.join(self.flat_files_dir, flat_file)) for flat_file in self.flat_files]
        self.fcomb = CombinedFlat(self.flats, ORDERS)
        self.fcomb.power_pixel_scale()

    def test_combination(self):
        return CombinedFlat([self.flat1, self.flat2], True).image

    def test_canny(self):
        # return Spline(self.test_spline()).canny()
        return self.fcomb.canny()

    def test_edges(self):
        return self.test_canny().edges

    def test_fill(self, seed_point):
        return self.test_canny().fill(seed_point)

    def test_locate(self):
        return self.fcomb.locate_orders()


fill_seed = ORDERS['ORDER_10']
fill_seed = (fill_seed['Y'], fill_seed['X'])
test = FlatTest(test_file_flat)
print('fcomb')
test.fcomb.show()
print(np.common_type(test.fcomb.image))
test.fcomb.image = test.fcomb.image.astype(np.int32)
test.fcomb.save(os.path.join(test_file_dir, 'fcomb.fits'))
test.fcomb.canny()
ArrayImage(test.fcomb.edges).show()
print('canny')
# ArrayImage(test.test_fill(fill_seed)).show()
test.test_canny().show_edges_overlay()
test.test_canny().show_fill_overlay(fill_seed)
test.test_locate().show_all_fill_overlay()
# test.test_canny()
