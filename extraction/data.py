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

# TODO: Need bad pixel mask
# TODO: Need cosmic ray mask
