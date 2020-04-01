from xspectre.utils.image import ListImage


class ListFlat(ListImage):
    def __init__(self, flats):
        super(ListFlat, self).__init__(images=flats)

    def generate_hot_pixel_map(self):
        # TODO: make this do something
        pass

    def generate_dead_pixel_mask(self, dead_pixel_value=65535):
        return self.image == dead_pixel_value
