import os
from pyspextool.extraction.data import Data
from pyspextool.utils.image import ExistingImage
from pyspextool import test
from matplotlib import pyplot as plt
import numpy as np

csv_file = os.path.join(test.extraction_output_dir, test.hk_arcs['Xe'].replace('.fits', '.csv'))
test_file = test.hk_arcs_input['Xe']
wavmap_file = os.path.join(test.test_file_dir, 'models', 'HK_wavmap.fits')
data = Data(test_file, test.extraction_output_dir, 0)
wavelength_map = ExistingImage(wavmap_file, 1)
wavelengths, intensities = data.quick_look_spectrum(wavelength_map.image)
save_array = np.asarray((wavelengths, intensities))
save_array = save_array.transpose()
np.savetxt(csv_file, save_array, delimiter=',')
plt.plot(wavelengths, intensities)
plt.show()
