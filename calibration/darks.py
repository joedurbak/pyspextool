from utils.image import ExistingImage, BaseImage
import numpy as np
import settings
import os


class Dark(ExistingImage):
    def __init__(self, filename, fits_image_hdu=settings.FITS_IMAGE_HDU):
        super(Dark, self).__init__(filename, fits_image_hdu)

    def generate_hot_pixel_mask(self, cutoff_percentile=90):
        return self.image > np.percentile(self.image, cutoff_percentile)


class DarkCombined(BaseImage):
    def __init__(self, darks):
        """
        Does all of the order locating and background removal for flats
        :param darks: expecting list of Flat containing Dark.image of the same shape
        :type darks: list
        """
        super(DarkCombined, self).__init__()
        self.darks = darks
        self.image = np.mean(np.asarray([dark.image for dark in darks]), axis=0)

    def generate_nonlinear_pixel_mask(
            self, time_array=None, linearity_error=0.1, image_base_value=0, ascending_counts=True
    ):
        if ascending_counts:
            image_sign = 1
        else:
            image_sign = -1

        darks_stacked = np.dstack([image_sign * dark.image - image_sign * image_base_value for dark in self.darks])
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


def test(dark_dir, hdu=0):
    dark_dir_list = os.listdir(dark_dir)
    dark_dir_list_fits = []
    for file in dark_dir_list:
        if file.endswith('.fits'):
            dark_dir_list_fits.append(os.path.join(dark_dir, file))
    dark_dir_list_fits.sort()
    darks = [Dark(file, hdu) for file in dark_dir_list_fits]
    return DarkCombined(darks)
