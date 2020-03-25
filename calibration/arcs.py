from pyspextool.utils.image import CombinedImage


class CombinedArc(CombinedImage):
    def __init__(self, arcs, order_map):
        super(CombinedArc, self).__init__(arcs)
        self.order_map = order_map

    def locate_peaks(self):
        # TODO: make this do something
        pass

    def wavelength_solution(self):
        # TODO: make this do something
        pass
