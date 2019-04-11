from utils.image import ExistingImage


class Data(ExistingImage):
    def __init__(self, filename):
        super(Data, self).__init__(filename)

    def linearity_correction(self):
        # TODO: find Vicki Toy's non-linearity correction for the H2RG detectors
        # TODO: find Vicki Toy's data in order to attempt Legendre Polynomial expansion
        pass

    def subtract_dark_telescope_sky(self, dark_telescope_sky, flat):
        self.image = (self.image-dark_telescope_sky)/flat

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


class DataWithExtractionParameters(Data):
    def __init__(self, filename):
        super(DataWithExtractionParameters, self).__init__(filename)
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
