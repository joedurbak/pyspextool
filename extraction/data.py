from pyspextool.utils.image import ExistingImage
import numpy as np


class Data(ExistingImage):
    def __init__(self, filename, calibration_directory, fits_image_hdu):
        super(Data, self).__init__(filename, fits_image_hdu)
        self.calibration_directory = calibration_directory

    def d_equals_b_minus_a_divided_by_flat(self, a, flat):
        # TODO: only make this happen within the located orders
        self.image = (self.image-a.image)/flat.image

    def create_spatial_overlay(self):
        # TODO: Convert code from mc_mkspatprof2d.pro
        pass

    def locate_apertures(self):
        # TODO: locate maxima for each column, and find optimal width (possibly for each column)
        #  then do smooth fit to reduce noise
        pass

    def trace_spectra(self):
        # TODO: look at pysalt to see how they accomplish this
        pass

    def define_extraction_parameters(self):
        # TODO: make this work
        pass

    def extract_spectra(self):
        pass

    def wavelength_calibrated_spectra(self):
        pass

    def quick_look_spectrum(self, wavelength_map):
        wavelengths = np.unique(wavelength_map)
        print(wavelengths)
        wavelengths = wavelengths[wavelengths > wavelengths.max()/2]
        # TODO: fix the resize so that this lazy threshold solution is unnecessary
        intensities = np.asarray([np.sum(self.image[wavelength_map == wavelength]) for wavelength in wavelengths])
        return wavelengths, intensities


class DataWithExtractionParameters(Data):
    def __init__(self, filename, calibration_directory):
        super(DataWithExtractionParameters, self).__init__(filename, calibration_directory)
        # point source
        self.psf_radius = -9999
        self.aperture_radius = -9999
        self.background_start = -9999
        self.background_width = -9999
        self.background_fit_degree = -9999
        # extended source
        self.aperture_radii = []
        self.background_regions = []
        self.background_fit_degree = -9999
