import os
from calibration.flats import FlatCombined, Flat
import settings


class CalibrationPacket:
    def __init__(self, save_dir, flat_dir=None, dark_dir=None, bad_pixel_map=None, orders=None):
        if flat_dir is not None:
            if orders is None:
                orders = settings.ORDERS
            flat = FlatCombined([Flat(os.path.join(flat_dir, file)) for file in os.listdir(flat_dir)], orders)
