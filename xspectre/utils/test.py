import os
from xspectre import test
from xspectre.utils.image import ExistingImage  # , image_overlay, ArrayImage

# create image object
test_image = ExistingImage(test.yj_flats_input[0], 0)
# test_image.show()

# resizing, translating image
test_image.scale_and_translate(269, 161, -1/0.925, -1/0.93, 0.5)
test_image.scale_and_translate(-269, -161, 0.925, 0.93, 0.5)
test_image.scale_and_translate(0, 0, -1, -1, 0)

# rotating image
test_image.rotate(1)
test_image.rotate(-1)

# save file
test_image.save(os.path.join(test.utils_output_dir, test.hk_flats[0]), hdu=0)

# intensity histogram
test_histogram_save_loc = os.path.join(test.utils_output_dir, 'histogram.png')
test_image.histogram(save_filepath=test_histogram_save_loc, show_plot=False, save_plot=True)
