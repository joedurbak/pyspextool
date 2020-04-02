import os

from matplotlib import pyplot as plt
import numpy as np

from xspectre.extraction.data import Data
from xspectre.utils.image import ExistingImage
from xspectre import test

if __name__ == '__main__':
    csv_file = os.path.join(test.extraction_output_dir, test.hk_arcs['Xe'].replace('.fits', '.csv'))
    test_file = test.hk_arcs_input['Xe']
    wavmap_file = os.path.join(test.test_file_dir, 'models', 'HK_wavmap.fits')

    print("CSV File:", csv_file)
    print("Test File:", test_file)
    print("Wavmap File:", wavmap_file)
    zzz

    data = Data(test_file, test.extraction_output_dir, 0)
    wavelength_map = ExistingImage(wavmap_file, 1)
    wavelengths, intensities = data.quick_look_spectrum(wavelength_map.image)

    save_array = np.asarray((wavelengths, intensities))
    save_array = save_array.transpose()
    
    np.savetxt(csv_file, save_array, delimiter=',')

    plt.figure()
    plt.plot(wavelengths, intensities)
    plt.xlabel('Wavelengths')
    plt.ylabel('Intensities')
    plt.show()
