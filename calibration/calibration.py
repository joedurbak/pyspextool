import os
from calibration.flats import FlatCombined


class CalibrationPacket:
    def __init__(self, save_dir, flat_dir=None, dark_dir=None, bad_pixel_map=None):
        if flat_dir is not None:
            flat = FlatCombined(os.listdir(flat_dir))
