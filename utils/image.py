from matplotlib import pyplot as plt
from astropy.io import fits
import settings
import numpy as np
import os
from PIL import Image
from random import randint
from . import errors
from skimage import filters
from skimage.morphology import disk
import cv2
from lacosmic import lacosmic
from scipy import interpolate
from collections.abc import Iterable


class BaseImage:
    """
    BaseImage class creates an object with all of the general image manipulation techniques
    """
    def __init__(self):
        self.image = None
        self.header = fits.Header()

    def show(self):
        """
        Displays the current image using pyplot
        :return:
        :rtype:
        """
        plt.figure(randint(0, 256))
        plt.imshow(self.image,)
        plt.xticks([]), plt.yticks([])
        plt.show()

    def save(self, filename):
        """
        saves image and header to fits file
        :param filename: file path to save to
        :type filename: str
        :return:
        :rtype:
        """
        # TODO: fix header saving issue
        file_dir = os.path.dirname(filename)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        hdu_primary = fits.PrimaryHDU(header=self.header)
        hdu_image = fits.ImageHDU(self.image)
        hdu_list = fits.HDUList([hdu_primary, hdu_image])
        hdu_list.writeto(filename, overwrite=True)

    def histogram(
            self, bin_width='auto', histogram_range=(), x_range=(), y_range=(), show_plot=False, save_plot=False,
            save_filepath="histogram.txt"
    ):
        """
        creates intensity histogram of the image
        :param bin_width: width of histogram bins
        :type bin_width: int or sequence or str, optional
        :param histogram_range:
        :type histogram_range:
        :param x_range:
        :type x_range:
        :param y_range:
        :type y_range:
        :param show_plot: determines if you want the histogram plot to show
        :type show_plot: bool
        :param save_plot:
        :type save_plot:
        :param save_filepath:
        :type save_filepath:
        :return:
        :rtype:
        """
        if histogram_range == ():
            histogram_range = (self.image.min(), self.image.max())
        y_max, x_max = self.image.shape
        if x_range == ():
            x_range = (0, x_max-1)
        if y_range == ():
            y_range = (0, y_max-1)
        a = self.image[y_range[0]:y_range[1]][x_range[0]:x_range[1]]
        a = a.flatten()
        histogram = np.histogram(a, bin_width, histogram_range)
        if show_plot or save_plot:
            plt.figure(randint(0, 256))
            plt.hist(a, bin_width, histogram_range)
            plt.title('Image Intensity Histogram')
            plt.ylabel('Intensity')
            if show_plot:
                plt.show()
            if save_plot:
                plt.savefig(save_filepath)
        return histogram

    def masked_interpolation(self, bad_pixel_mask, method='cubic'):
        bad_pixel_mask = bad_pixel_mask > 0
        x = np.arange(0, self.image.shape[1])
        y = np.arange(0, self.image.shape[0])
        self.image[bad_pixel_mask] = np.nan
        self.image = np.ma.masked_invalid(self.image)
        xx, yy = np.meshgrid(x, y)
        x1 = xx[~self.image.mask]
        y1 = yy[~self.image.mask]
        newarr = self.image[~self.image.mask]
        assert isinstance(x1, np.ndarray)
        assert isinstance(y1, np.ndarray)
        self.image = interpolate.griddata((x1, y1), newarr.ravel(), (xx, yy), method=method)

    def median_filter(self, disk_radius=2):
        """
        Replaces pixel value with median of neighborhood
        :param disk_radius: radius needed for median
        :type disk_radius: int
        :return: alters self.image
        :rtype: None
        """
        # TODO: figure out why this isn't working, consider using astropy.convolution instead
        self.image = filters.median(self.image, selem=disk(disk_radius))

    def mean_filter(self, disk_radius=2):
        """
        Replaces pixel value with mean of neighborhood
        :param disk_radius: radius needed for mean
        :type disk_radius: int
        :return: alters self.image
        :rtype: None
        """
        # TODO: figure out why this isn't working, consider using astropy.convolution instead
        self.image = filters.rank.mean(self.image, selem=disk(disk_radius))

    def cosmic_filter(
            self, contrast, cr_threshold, neighbor_threshold, error=None, mask=None, background=None,
            effective_gain=None, readnoise=None, maxiter=4, border_mode=u'mirror'
            ):
        """
        Cleans cosmic rays from image using lacosmic algorithm
        :param contrast:
        :type contrast:
        :param cr_threshold:
        :type cr_threshold:
        :param neighbor_threshold:
        :type neighbor_threshold:
        :param error:
        :type error:
        :param mask:
        :type mask:
        :param background:
        :type background:
        :param effective_gain:
        :type effective_gain:
        :param readnoise:
        :type readnoise:
        :param maxiter:
        :type maxiter:
        :param border_mode:
        :type border_mode:
        :return:
        :rtype:
        """
        # TODO: figure out which parameters work best for this. Ask JWST folks, Dale or Bernie, what they used for this
        self.image = lacosmic(
            self.image, contrast=contrast, cr_threshold=cr_threshold, neighbor_threshold=neighbor_threshold,
            error=error, mask=mask, background=background, effective_gain=effective_gain, readnoise=readnoise,
            maxiter=maxiter, border_mode=border_mode
        )

    def slice(self, x_range=(), y_range=()):
        """
        Selects part of the image
        :param x_range: min and max for slice
        :type x_range: Iterable
        :param y_range: min and max for slice
        :type y_range: Iterable
        :return:
        :rtype:
        """
        # TODO: determine if we actually want it to replace the image, or return another array
        y_max, x_max = self.image.shape
        if x_range == ():
            x_range = (0, x_max)
        if y_range == ():
            y_range = (0, y_max)
        self.image = self.image[y_range[0]:y_range[1], x_range[0]:x_range[1]]

    def border(self, x_left=0, x_right=0, y_top=0, y_bottom=0, border_value=0):
        """
        adds a border around image
        :param x_left: adds border before 0th index along axis=1
        :type x_left: int
        :param x_right: adds border after maximum index along axis=1
        :type x_right: int
        :param y_top: adds border after maximum index along axis=0
        :type y_top: int
        :param y_bottom: adds border before 0th index along axis=0
        :type y_bottom: int
        :param border_value: pixel value of added border
        :type border_value: int
        :return:
        :rtype: None
        """
        y_max, x_max = self.image.shape
        border_array = np.zeros((y_top+y_max+y_bottom, x_left+x_max+x_right)) + border_value
        border_array[y_bottom:y_bottom+y_max, x_left:x_left+x_max] = self.image
        self.image = border_array

    def resize(self, width_scale_factor=1, height_scale_factor=1):  # , resample=0):
        if width_scale_factor < 0:
            self.image = np.flip(self.image, 1)
            width_scale_factor = np.abs(width_scale_factor)
        if height_scale_factor < 0:
            self.image = np.flip(self.image, 0)
            height_scale_factor = np.abs(height_scale_factor)
        pil_image = Image.fromarray(self.image)
        width, height = pil_image.size
        width = width * width_scale_factor
        width = int(width)
        height = height * height_scale_factor
        height = int(height)
        pil_image_resize = pil_image.resize((width, height), resample=Image.NEAREST)
        self.image = np.array(pil_image_resize)

    def translate(self, x_translation, y_translation):
        self.image = np.roll(self.image, x_translation)
        self.image = np.roll(self.image, y_translation, axis=0)

    def crop_and_border(self, x_size, y_size, border_value=0):
        y_size_initial, x_size_initial = self.image.shape
        x_start = int((x_size_initial - x_size)/2)
        y_start = int((y_size_initial - y_size)/2)
        if x_start > 0:
            self.slice(x_range=(x_start, x_start+x_size))
        elif x_start < 0:
            x_start = -x_start
            x_size_difference = x_size - (2 * x_start + x_size_initial)
            self.border(
                x_left=x_start, x_right=x_start+x_size_difference, y_top=0, y_bottom=0, border_value=border_value
            )
        if y_start > 0:
            self.slice(y_range=(y_start, y_start+y_size))
        elif y_start < 0:
            y_start = -y_start
            y_size_difference = y_size - (2 * y_start + y_size_initial)
            self.border(
                x_left=0, x_right=0, y_top=y_start, y_bottom=y_start+y_size_difference, border_value=border_value
            )

    def scale_and_translate(self, x_translation=0, y_translation=0, x_scale=1, y_scale=1, border_value=0):
        # , resample=0):
        x_size_initial, y_size_initial = self.image.shape
        self.resize(x_scale, y_scale)  # , resample=resample)
        self.crop_and_border(x_size_initial, y_size_initial, border_value=border_value)
        self.translate(x_translation, y_translation)

    def power_pixel_scale(self, a=1000):
        x = self.image/np.max(self.image)
        self.image = (a**x-1)/a

    def rotate(self, angle_degrees):
        image_center = tuple(np.array(self.image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle_degrees, 1.0)
        result = cv2.warpAffine(self.image, rot_mat, self.image.shape[1::-1], flags=cv2.INTER_NEAREST)
        self.image = result

    def linearity_correction(self):
        # TODO: find Vicki Toy's non-linearity correction for the H2RG detectors
        # TODO: find Vicki Toy's data in order to attempt Legendre Polynomial expansion
        pass

    def min_max_intensity_manipulate(self, minimum, maximum):
        min_max_intensity_manipulate(self.image, minimum, maximum)


class ExistingImage(BaseImage):
    def __init__(self, filename: str, fits_image_hdu=settings.FITS_IMAGE_HDU):
        super(ExistingImage, self).__init__()
        self.filename = filename
        self.hdu_list = fits.open(filename)
        self.image = self.hdu_list[fits_image_hdu].data
        if self.image is None:
            raise errors.EmptyImageError("Selected image HDU contains no array")
        self.header = self.hdu_list[0].header


class PNGImage(BaseImage):
    def __init__(self, filename):
        super(PNGImage, self).__init__()
        self.image = np.mean(plt.imread(filename,), -1)


class ArrayImage(BaseImage):
    def __init__(self, array):
        super(ArrayImage, self).__init__()
        self.image = array


class ListImage(BaseImage):
    def __init__(self, images):
        super(ListImage, self).__init__()
        self.images = [image.image for image in images]

    def linearity_check(self):
        pass


class CombinedImage(ListImage):
    def __init__(self, images):
        super(CombinedImage, self).__init__(images)
        self.image = np.mean(self.images)


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
    plt.figure()
    plt.imshow(background_image, interpolation='nearest', cmap=background_cmap)
    plt.imshow(foreground_image, interpolation='bilinear', alpha=0.5)
    plt.yticks([])
    plt.xticks([])
    plt.show()


def min_max_intensity_manipulate(image, minimum, maximum):
    image[image < minimum] = minimum
    image[image > maximum] = maximum
