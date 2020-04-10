from xspectre.utils.image import CombinedImage, ExistingImage, ArrayImage
from xspectre.test import hk_wave_map_model


class CombinedArc(CombinedImage):
    def __init__(self, arcs, order_map, bad_pixel_map=None):
        super(CombinedArc, self).__init__(arcs, bad_pixel_map=bad_pixel_map)
        self.order_map = order_map

    def locate_peaks(self):
        # TODO: make this do something
        pass

    def wavelength_solution(self):
        # TODO: make this do something
        pass

    def wavelength_map(self):
        # TODO: make this work via calibration
        return ExistingImage(hk_wave_map_model, fits_image_hdu=1).image

    def wavelength_map_image(self):
        return ArrayImage(self.wavelength_map())
