from xspectre.calibration.flats import CombinedFlat, Flat
from xspectre import test
from xspectre.utils.image import ArrayImage
from xspectre.settings import ORDERS_RIMAS as ORDERS
import os
import numpy as np
# import numpy as np


class FlatTest:
    def __init__(self, test_filenames):
        self.flats = [Flat(flat_file) for flat_file in test_filenames]
        self.fcomb = CombinedFlat(self.flats, ORDERS)
        self.fcomb.power_pixel_scale()

    def test_combination(self):
        return CombinedFlat(self.flats, True).image

    def test_canny(self):
        # return Spline(self.test_spline()).canny()
        return self.fcomb.canny()

    def test_edges(self):
        return self.test_canny().edges

    def test_fill(self, seed_point):
        return self.test_canny().fill(seed_point)

    def test_locate(self):
        return self.fcomb.locate_orders()


fill_seed = ORDERS[10]
fill_seed = (fill_seed['Y'], fill_seed['X'])
flat_test = FlatTest(test.hk_flats[0])
flat_test.fcomb.show()
flat_test.fcomb.image = flat_test.fcomb.image.astype(np.int32)
flat_test.fcomb.save(os.path.join(test.characterization_output_dir, 'flats_combined.fits'))
flat_test.fcomb.canny()
ArrayImage(flat_test.fcomb.edges).show()
# ArrayImage(test.test_fill(fill_seed)).show()
flat_test.test_canny().show_edges_overlay()
flat_test.test_canny().show_fill_overlay(fill_seed)
flat_test.test_locate().show_all_fill_overlay()
# test.test_canny()
