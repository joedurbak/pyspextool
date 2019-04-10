from calibration.arcs import ArcCombined, Arc
from calibration.flats import FlatCombined, Flat
from astroquery.nist import Nist
from settings import ARCS
import astropy.units as u

ARCS[0]['ELEMENT']
q = Nist.query(900*u.nm, 2400*u.nm, 'Xe', output_order='wavelength', wavelength_type='vacuum')
