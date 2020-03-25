import numpy as np
from pyspextool.utils.image import BaseImage, ExistingImage, image_overlay, CombinedImage
from pyspextool.utils.frames import Flat
from skimage import feature
from skimage.segmentation import flood_fill
import settings


class CombinedFlat(CombinedImage):
    def __init__(self, flats, orders, scale_flats=False, sigma=5):
        """
        Does all of the order locating and background removal for flats
        :param flats: expecting list of Flat containing Flat.image of the same shape
        :type flats: list
        :param scale_flats: determines whether all flats are normalized or added as is, increases comp time
        :type scale_flats: bool
        """
        super(CombinedFlat, self).__init__(flats)
        self.scaled_flats = [flat.scale_flat(scale_flats) for flat in flats]
        # self.array_and_scale = np.asarray(
        #     [np.asarray((flat.image, flat.flat_scale_multiplier)) for flat in self.scaled_flats])
        # self.image = np.sum(self.array_and_scale[:, 0]) * np.mean(self.array_and_scale[:, 1])
        # self.image = np.mean(np.asarray([flat.image for flat in flats]), axis=0)
        # print(self.image)
        self.edges = None
        self.orders = orders
        self.sigma = sigma
        # self.locate_orders()

    def canny(self):
        self.edges = feature.canny(self.image, sigma=self.sigma)
        # TODO: spline edges

    def fill(self, seed_point, fill_value=3):
        y, x = self.edges.shape
        mask = np.zeros((y, x))
        filled_mask = mask.copy()
        mask[:, :x - 1] = self.edges[:, 1:x]
        mask = mask + self.edges
        mask = mask[1:y - 1, 0:x - 1]
        k = 0
        while int(mask[seed_point]) != 0:
            j, i = seed_point
            i += 1
            k += 1
            if k == 6:
                raise ValueError
        filled_mask[1:y - 1, 0:x - 1] = flood_fill(mask, seed_point, fill_value)
        return filled_mask[filled_mask > 2]

    def locate_orders(self):
        self.canny()
        for order_dict in self.orders:
            # TODO: Set up multi-threading for this process
            print(order_dict)
            print((order_dict['Y'], order_dict['X']))
            order_dict['order_location_array'] = self.fill((order_dict['Y'], order_dict['X']))
            self.orders[order] = order_dict

    def normalized_flat(self):
        return self.image / np.max(self.image)

    def show_edges_overlay(self):
        image_overlay(self.image, self.edges)

    def show_fill_overlay(self, seed_point):
        image_overlay(self.image, self.fill(seed_point))

    def show_all_fill_overlay(self):
        fill_image = np.zeros(self.image.shape)
        for order, order_dict in self.orders.items():
            fill_image += order_dict['order_location_array']
        image_overlay(self.image, fill_image)

    # def generate_cold_pixel_mask(self, cutoff_percentile=10):
    #     return self.image < np.percentile(self.image, cutoff_percentile)
    # 
    def generate_dead_pixel_mask(self, dead_pixel_value=65535):
        return self.image == dead_pixel_value
