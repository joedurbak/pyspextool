import os
from calibration.flats import CombinedFlat

# TODO: make this the main file to interact with the calibration module


class CalibrationPacket:
    # TODO: come up with a good way to save, open different calibration packets
    def __init__(self, save_dir, flat_dir=None, dark_dir=None, bad_pixel_map=None):
        if flat_dir is not None:
            flat = CombinedFlat(os.listdir(flat_dir))
