import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NORMALIZE_FLATS = False
FITS_IMAGE_HDU = 0
ORDERS = [
    {
        'X': 70, 'Y': 200,  # rough center of order
        'M': 1,  # order value
    },
    {
        'X': 100, 'Y': 170,  # rough center of order
        'M': 2,
    },
    {
        'X': 100, 'Y': 130,  # rough center of order
        'M': 3,
    },
    {
        'X': 100, 'Y': 90,  # rough center of order
        'M': 4,
    },
    {
        'X': 100, 'Y': 50,  # rough center of order
        'M': 5,
    },
    {
        'X': 175, 'Y': 25,  # rough center of order
        'M': 6,
    },
]

ORDERS_YJ = [
    {
        'X': 1440, 'Y': 975,  # rough center of order
        'M': 30,  # order value
    },
    {
        'X': 1380, 'Y': 975,  # rough center of order
        'M': 31,  # order value
    },
    {
        'X': 1320, 'Y': 975,  # rough center of order
        'M': 32,  # order value
    },
    {
        'X': 1260, 'Y': 975,  # rough center of order
        'M': 33,  # order value
    },
    {
        'X': 1210, 'Y': 975,  # rough center of order
        'M': 34,  # order value
    },
    {
        'X': 1160, 'Y': 975,  # rough center of order
        'M': 35,  # order value
    },
    {
        'X': 1110, 'Y': 975,  # rough center of order
        'M': 36,  # order value
    },
    {
        'X': 1060, 'Y': 975,  # rough center of order
        'M': 37,  # order value
    },
    {
        'X': 1020, 'Y': 975,  # rough center of order
        'M': 38,  # order value
    },
    {
        'X': 980, 'Y': 975,  # rough center of order
        'M': 39,  # order value
    },
    {
        'X': 940, 'Y': 975,  # rough center of order
        'M': 40,  # order value
    },
    {
        'X': 900, 'Y': 975,  # rough center of order
        'M': 41,  # order value
    },
    {
        'X': 860, 'Y': 975,  # rough center of order
        'M': 42,  # order value
    },
    {
        'X': 830, 'Y': 975,  # rough center of order
        'M': 43,  # order value
    },
    {
        'X': 790, 'Y': 975,  # rough center of order
        'M': 44,  # order value
    },
]

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

ORDERS_RIMAS = {
    'ORDER_1': {
        'X': 930, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_2': {
        'X': 960, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_3': {
        'X': 990, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_4': {
        'X': 1020, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_5': {
        'X': 1050, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_6': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_7': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_8': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_9': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_10': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_11': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_12': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_13': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_14': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_15': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_16': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_17': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_18': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
    'ORDER_19': {
        'X': 1080, 'Y': 1150,  # rough center of order
        'STARTING_WAVELENGTH': 0,
        'ENDING_WAVELENGTH': 0,
    },
}
