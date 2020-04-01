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

ORDERS_HK = [
    {
        'X': 935, 'Y': 1150,  # rough center of order
        'M': 39,
    },
    {
        'X': 960, 'Y': 1150,  # rough center of order
        'M': 38,
    },
    {
        'X': 990, 'Y': 1150,  # rough center of order
        'M': 37,
    },
    {
        'X': 1020, 'Y': 1150,  # rough center of order
        'M': 36,
    },
    {
        'X': 1060, 'Y': 1150,  # rough center of order
        'M': 35,
    },
    {
        'X': 1090, 'Y': 1150,  # rough center of order
        'M': 34,
    },
    {
        'X': 1130, 'Y': 1150,  # rough center of order
        'M': 33,
    },
    {
        'X': 1170, 'Y': 1150,  # rough center of order
        'M': 32,
    },
    {
        'X': 1210, 'Y': 1150,  # rough center of order
        'M': 31,
    },
    {
        'X': 1250, 'Y': 1150,  # rough center of order
        'M': 30,
    },
    {
        'X': 1300, 'Y': 1150,  # rough center of order
        'M': 29,
    },
    {
        'X': 1350, 'Y': 1150,  # rough center of order
        'M': 28,
    },
    {
        'X': 1400, 'Y': 1150,  # rough center of order
        'M': 27,
    },
    {
        'X': 1460, 'Y': 1150,  # rough center of order
        'M': 26,
    },
    {
        'X': 1520, 'Y': 1150,  # rough center of order
        'M': 25,
    },
    {
        'X': 1590, 'Y': 1150,  # rough center of order
        'M': 24,
    },
    {
        'X': 1660, 'Y': 1150,  # rough center of order
        'M': 23,
    },
]
