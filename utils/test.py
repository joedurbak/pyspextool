from utils.image import ExistingImage, image_overlay, ArrayImage
import os
import settings
import numpy as np

test_file_dir = os.path.join(settings.BASE_DIR, 'test', )
# test_file_flat = os.path.join(test_file_dir, 'flat.fits',)
# test_file_flat = os.path.join(test_file_dir, 'HK_dcurve_reflected.fits',)
# test_file_flat = os.path.join(test_file_dir, 'HK_dcurve.fits',)
test_file_flat = os.path.join(test_file_dir, 'HK_Hg_model.fits',)
test_file_sky_spectra = os.path.join(test_file_dir, 'RIMAS_OH_lines.fits',)
test_histogram_save_loc = os.path.join(settings.BASE_DIR, 'test', 'histogram.png')
test_image = ExistingImage(test_file_flat, 0)
# test_image.show()
# print(test_image.histogram(show_plot=True, save_plot=True, save_filepath=test_histogram_save_loc))
# test_image.resize(0.9, 0.7)
# test_image.scale_and_translate(0, 0, -1, -1, 1)
# test_image.save(test_file_flat+'.tmp')
test_image.scale_and_translate(269, 161, -1/0.925, -1/0.93, 0.5)
test_image.rotate(1)
output_file = os.path.join(test_file_dir, 'flat_scaled_rotated_and_translated.fits',)
test_image.save(output_file)


test_file_flat = os.path.join(test_file_dir, 'HK_wavmap.fits',)
test_image = ExistingImage(test_file_flat, 0)
test_image.scale_and_translate(269, 161, -1/0.925, -1/0.93, 0)  # , 1)
max_val = np.min(test_image.image[np.nonzero(test_image.image)])
test_image.image[test_image.image < max_val] = 0
test_image.rotate(1)
test_image.image[test_image.image < max_val] = 0
output_file = os.path.join(test_file_dir, 'HK_calibration', 'HK_wavmap_scaled_rotated_and_translated.fits',)
test_image.save(output_file)


# test_image.show()
# spectrum_image_file = os.path.join(test_file_dir, 'Hg_spectrum.fits',)
flat_image_file = os.path.join(test_file_dir, 'HK_flat.fits',)
spectrum_image_file = os.path.join(test_file_dir, 'HK_Xe_data.fits',)
# spectrum_image_file = os.path.join(test_file_dir, '20020103T002606C1-0006.fits',)
spectrum_image = ExistingImage(spectrum_image_file)
flat_image = ExistingImage(flat_image_file)
# spectrum_image.image = np.int64(spectrum_image.image)
# spectrum_image.show()
mask_file = os.path.join(test_file_dir, 'bad_pixels.fits')
# spectrum_image.masked_interpolation(ExistingImage(mask_file, 1).image, method='nearest')
# spectrum_image.show()
ArrayImage(spectrum_image.image).save(os.path.join(test_file_dir, 'nearest_interpolated.fits'))
# spectrum_image.median_filter()
# ArrayImage(spectrum_image.image).save(os.path.join(test_file_dir, 'median_filter.fits'))
# spectrum_image.mean_filter()
# ArrayImage(spectrum_image.image).save(os.path.join(test_file_dir, 'mean_filter.fits'))
# spectrum_image.show()
# spectrum_image.show()
image_overlay(flat_image.image, test_image.image)
image_overlay(spectrum_image.image, test_image.image)
spectrum_image_file = os.path.join(test_file_dir, 'HK_flat.fits',)
