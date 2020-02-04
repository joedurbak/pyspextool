import os
from extraction.data import Data
import settings
from utils.image import ExistingImage
from matplotlib import pyplot as plt
import numpy as np

test_file_dir = os.path.join(settings.BASE_DIR, 'test', )
csv_file = os.path.join(test_file_dir, 'HK_Hg_spectrum.csv')
# test_file = os.path.join(test_file_dir, 'Hg_spectrum.fits')
test_file = r'G:\My Drive\RIMAS spectra\spectra_upload_2019_10_18\20191018T132027C1-Char_run_Grisms_Xe\dark_subtracted\20191018T132027C1-0007.fits'
calibration_dir = os.path.join(test_file_dir, 'HK_calibration')
wavmap_file = os.path.join(calibration_dir, 'HK_wavmap_scaled_rotated_and_translated.fits')
data = Data(test_file, calibration_dir, 0)
wavelength_map = ExistingImage(wavmap_file, 1)
wavelengths, intensities = data.quick_look_spectrum(wavelength_map.image)
save_array = np.asarray((wavelengths, intensities))
save_array = save_array.transpose()
np.savetxt(csv_file, save_array, delimiter=',')
plt.plot(wavelengths, intensities)
plt.show()
