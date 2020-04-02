import numpy as np
from skimage import feature
from skimage.segmentation import flood_fill

from xspectre.utils.image import image_overlay, CombinedImage, ArrayImage

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

    def canny(self, manipulate_min=None, manipulate_max=None, mean_filter_disk_radius=None):
        canny_image = ArrayImage(self.image)
        if mean_filter_disk_radius is not None:
            canny_image.mean_filter(mean_filter_disk_radius)
        if manipulate_max is None:
            manipulate_max = canny_image.image.max()
        if manipulate_min is None:
            manipulate_min = canny_image.image.min()
        canny_image.min_max_intensity_manipulate(manipulate_min, manipulate_max)
        self.edges = feature.canny(
            canny_image.image, sigma=self.sigma,  # low_threshold=manipulate_min, high_threshold=manipulate_max,
        )
        # TODO: find a way to extract and fit a function to contours

    def fill(self, seed_point, fill_value=3):
        # TODO: replace this with something that doesn't risk flooding entire image
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

    def locate_orders(self, canny_image_min=None, canny_image_max=None):
        self.canny(canny_image_min, canny_image_max)
        order_map = np.zeros(self.image.shape).astype(np.int)
        for order_dict in self.orders:
            # TODO: Set up multi-threading for this process
            # print(order_dict)
            # print((order_dict['Y'], order_dict['X']))
            order = self.fill((order_dict['Y'], order_dict['X']))
            print("order after fill shape: {}".format(order.shape))
            order = order.astype(np.int)
            print("order after type change shape: {}".format(order.shape))
            order = order * order_dict['M']
            print("order after multiplication shape: {}".format(order.shape))
            order_map += order
        return order_map

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
