import os

import numpy as np

from xspectre.characterization.darks import ListDark
from xspectre.characterization.flats import ListFlat
from xspectre.test import hk_flats_input, characterization_output_dir
from xspectre.utils.frames import Flat, Dark
from xspectre.utils.image import ArrayImage

flats = [Flat(f) for f in hk_flats_input]
list_flat = ListFlat(flats)
bad_pixel_flats = list_flat.bad_pixel_array()
bad_pixel_flats_image = list_flat.bad_pixel_image()
bad_pixel_flats_image.save(os.path.join(characterization_output_dir, 'bad_pixel_flat_map.fits'), hdu=0)

darks = [Dark(d) for d in hk_flats_input]
list_dark = ListDark(darks)
bad_pixel_darks = list_dark.bad_pixel_array()
bad_pixel_darks_image = list_dark.bad_pixel_image()
bad_pixel_flats_image.save(os.path.join(characterization_output_dir, 'bad_pixel_dark_map.fits'), hdu=0)

bad_pixel_map = np.logical_or(bad_pixel_flats, bad_pixel_darks)
bad_pixel_map_image = ArrayImage(bad_pixel_map.astype(np.int16))
bad_pixel_map_image.save(os.path.join(characterization_output_dir, 'bad_pixel_map.fits'), hdu=0)
