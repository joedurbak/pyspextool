import os
from xspectre import settings

test_file_dir = os.path.join(settings.BASE_DIR, 'test', )
output_dir = os.path.join(test_file_dir, 'output')
calibration_output_dir = os.path.join(output_dir, 'calibration')
characterization_output_dir = os.path.join(output_dir, 'characterization')
extraction_output_dir = os.path.join(output_dir, 'extraction')
utils_output_dir = os.path.join(output_dir, 'utils')

hk_flats = ['hk_flat0.fits', 'hk_flat1.fits', 'hk_flat2.fits']
hk_flats_input = [os.path.join(test_file_dir, hk_flat) for hk_flat in hk_flats]
yj_flats = ['yj_flat0.fits', 'yj_flat1.fits', 'yj_flat2.fits']
yj_flats_input = [os.path.join(test_file_dir, yj_flat) for yj_flat in yj_flats]

hk_arcs = {
    'Hg': 'hk_arc_Hg.fits',
    'Kr': 'hk_arc_Xe.fits',
    'Ar': 'hk_arc_Ar.fits',
    'Xe': 'hk_arc_Xe.fits',
}

yj_arcs = {
    'Hg': 'yj_arc_Hg.fits',
    'Kr': 'yj_arc_Xe.fits',
    'Ar': 'yj_arc_Ar.fits',
    'Xe': 'yj_arc_Xe.fits',
}

hk_arcs_input = {}

for key, value in hk_arcs.items():
    hk_arcs_input[key] = os.path.join(test_file_dir, value)

yj_arcs_input = {}

for key, value in yj_arcs.items():
    yj_arcs_input[key] = os.path.join(test_file_dir, value)
