import os

import numpy as np

from xspectre.utils.image import ListImage, ArrayImage
from xspectre.utils.frames import Dark


class ListDark(ListImage):
    def __init__(self, darks):
        """
        Characterizes detector based on dark frames

        Main output for this class is given by the bad_pixel_image function

        Parameters
        ----------
        darks : list
            list of Dark image objects
        """
        super(ListDark, self).__init__(darks)
        self.hot_pixel_mask = None

    def generate_hot_pixel_mask(self):
        # TODO: make this do something
        pass

    def generate_nonlinear_pixel_mask(
            self, time_array=None, linearity_error=0.1, image_base_value=0, ascending_counts=True
    ):
        # TODO: pick a different method for this. this doesn't really work
        # TODO: consider making this a part of utils.image.ListImage instead
        if ascending_counts:
            image_sign = 1
        else:
            image_sign = -1

        darks_stacked = np.dstack([image_sign * dark.image - image_sign * image_base_value for dark in self.images])
        if np.min(darks_stacked) <= 0:
            raise ValueError("All image values must be greater than zero")
        # darks_stacked = darks_stacked[:, :, 1:] - darks_stacked[:, :, 0]
        darks_stacked_log = np.log(darks_stacked)
        if time_array is None:
            time_array_length = darks_stacked[0, 0].shape[0]
            time_array = np.arange(0, time_array_length, 1)
            # time_array[0] = 10**-9
        # time_array = time_array[1:] - time_array[0]
        time_array_log = np.log(time_array[1:])
        y_shape, x_shape, z_shape = darks_stacked_log.shape
        linear_coefficient_log_log = np.zeros((y_shape, x_shape))
        for y in range(y_shape):
            for x in range(x_shape):
                try:
                    linear_coefficient_log_log[y, x] = np.polyfit(time_array_log, darks_stacked_log[y, x, 1:], 1)[0]
                except np.linalg.linalg.LinAlgError:
                    linear_coefficient_log_log[y, x] = -1
        # mask = (1-linearity_error) < linear_coefficient_log_log < (1+linearity_error)
        return linear_coefficient_log_log

    def bad_pixel_array(self):
        return np.random.rand(*self.images[0].shape) > 0.95

    def bad_pixel_image(self):
        return ArrayImage(self.bad_pixel_array().astype(np.int16))


def test(dark_dir, hdu=0):
    dark_dir_list = os.listdir(dark_dir)
    dark_dir_list_fits = []
    for file in dark_dir_list:
        if file.endswith('.fits'):
            dark_dir_list_fits.append(os.path.join(dark_dir, file))
    dark_dir_list_fits.sort()
    darks = [Dark(file, hdu) for file in dark_dir_list_fits]
    return ListDark(darks)
