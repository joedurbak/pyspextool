import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NORMALIZE_FLATS = False
FITS_IMAGE_HDU = 0
ORDERS = {
    'ORDER_1': {
        'X': 70, 'Y': 200,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_2': {
        'X': 100, 'Y': 170,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_3': {
        'X': 100, 'Y': 130,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_4': {
        'X': 100, 'Y': 90,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_5': {
        'X': 100, 'Y': 50,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_6': {
        'X': 175, 'Y': 25,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
}

ARCS = [
    {
        'ELEMENT': 'Xe',
        'FILENAME': '',
    },
    {
        'ELEMENT': '',
        'FILENAME': '',
    }
]
