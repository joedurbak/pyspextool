from utils.image import ExistingImage
import numpy as np
import settings


class Dark(ExistingImage):
    def __init__(self, filename, fits_image_hdu=settings.FITS_IMAGE_HDU):
        super(Dark, self).__init__(filename, fits_image_hdu)

    def generate_hot_pixel_mask(self, cutoff_percentile=90):
        return self.image > np.percentile(self.image, cutoff_percentile)


class Flat(ExistingImage):
    def __init__(self, filename, fits_image_hdu=settings.FITS_IMAGE_HDU):
        super(Flat, self).__init__(filename=filename, fits_image_hdu=fits_image_hdu)
        self.flat_scale_multiplier = 1

    def scale_flat(self, scale_activated=False):
        if scale_activated:
            self.flat_scale_multiplier = np.mean(self.image)
            self.image = self.image / self.flat_scale_multiplier
        return self

    def generate_dead_pixel_mask(self, dead_pixel_value=65535):
        return self.image == dead_pixel_value


class Arc(ExistingImage):
    def __init__(self, filename):
        super(Arc, self).__init__(filename)

