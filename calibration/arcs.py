from utils.image import BaseImage, ExistingImage
import numpy as np


class Arc(ExistingImage):
    def __init__(self, filename):
        super(Arc, self).__init__(filename)


class ArcCombined(BaseImage):
    def __init__(self, arcs):
        super(ArcCombined, self).__init__()
        self.image = np.sum([arc.image for arc in arcs])
