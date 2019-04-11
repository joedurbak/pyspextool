from matplotlib import pyplot as plt
from astropy.io import fits
import settings
import numpy as np


class BaseImage:
    def __init__(self):
        self.image = None
        self.header = fits.Header()

    def show(self):
        plt.imshow(self.image,)
        plt.xticks([]), plt.yticks([])
        plt.show()

    def save(self, filename):
        hdu_primary = fits.PrimaryHDU(header=self.header)
        hdu_image = fits.ImageHDU(self.image)
        hdu_list = fits.HDUList([hdu_primary, hdu_image])
        hdu_list.writeto(filename)

    def bad_pixel_mask(self):
        # TODO: Need bad pixel mask
        pass

    def cosmic_ray_filter(self):
        # TODO: Need cosmic ray mask
        pass


class ExistingImage(BaseImage):
    def __init__(self, filename: str):
        super(ExistingImage, self).__init__()
        self.filename = filename
        self.hdu_list = fits.open(filename)
        self.image = self.hdu_list[settings.FITS_IMAGE_HDU].data
        if self.image is None:
            raise FileNotFoundError
        self.header = self.hdu_list[0].header


class PNGImage(BaseImage):
    def __init__(self, filename):
        super(PNGImage, self).__init__()
        self.image = np.mean(plt.imread(filename,), -1)


class ArrayImage(BaseImage):
    def __init__(self, array):
        super(ArrayImage, self).__init__()
        self.image = array


def image_overlay(background_image, foreground_image, background_cmap='Greys'):
    """
    Plots foreground over background image
    :param background_image: background image
    :type background_image: np.array
    :param foreground_image: foreground image
    :type foreground_image: np.array
    :param background_cmap: color map for background
    :type background_cmap: string
    :return:
    :rtype:
    """
    bkgrnd_img = plt.imshow(background_image, interpolation='nearest', cmap=background_cmap)
    frgrnd_img = plt.imshow(foreground_image, interpolation='bilinear', alpha=0.5)
    plt.yticks([])
    plt.xticks([])
    plt.show()
