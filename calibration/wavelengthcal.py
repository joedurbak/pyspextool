from pyspextool.calibration.arcs import CombinedArc
from pyspextool.calibration.flats import CombinedFlat, Flat
from astroquery.nist import Nist
from pyspextool.settings import ARCS
import astropy.units as u

# TODO: determine whether or not to keep this file


ARCS[0]['ELEMENT']
q = Nist.query(900*u.nm, 2400*u.nm, 'Xe', output_order='wavelength', wavelength_type='vacuum')
