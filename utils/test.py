from utils.image import ExistingImage
import os
import settings

test_file = os.path.join(settings.BASE_DIR, 'test',)
test_file = os.path.join(test_file, 'flat.fits',)
# ExistingImage(test_file).show()
