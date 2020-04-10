import os

from matplotlib import pyplot as plt
import numpy as np

from xspectre.extraction.data import Data
from xspectre.utils.image import ExistingImage
from xspectre import test

if __name__ == '__main__':
    csv_file = os.path.join(test.extraction_output_dir, test.hk_arcs['Xe'].replace('.fits', '.csv'))
    test_file = test.hk_arcs_input['Xe']
    # wavmap_file = os.path.join(test.test_file_dir, 'models', 'HK_wavmap.fits')
    normalized_flat = np.ones(ExistingImage(test_file).image.shape)
    wavelength_map = ExistingImage(test.hk_wave_map_model, fits_image_hdu=1).image
    order_map = ExistingImage(test.hk_order_map_model, fits_image_hdu=1).image
    data = Data(
        test_file, wavelength_map=wavelength_map, order_map=order_map,
        normalized_flat=normalized_flat, bad_pixel_map=None,
        calibration_directory=test.extraction_output_dir, fits_image_hdu=0
    )
    wavelengths, intensities = data.quick_look_spectrum()

    save_array = np.asarray((wavelengths, intensities))
    save_array = save_array.transpose()
    
    np.savetxt(csv_file, save_array, delimiter=',')

    plt.figure()
    plt.plot(wavelengths, intensities)
    plt.xlabel('Wavelengths')
    plt.ylabel('Intensities')
    plt.show()
