import os
import json

def load_default():
    '''Load the default settings'''
    fn = 'settings_default.json'
    with open(fn) as fp:
        data = json.load(fp)

    data['base_dir'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return data

def load_json(fn):
    '''Load a JSON settings file

    Params
    ------
    fn : str
        Filename of the JSON settings file

    Notes
    -----
    Any settings not in the JSON file are set to their default values
    '''

    data = load_default()
    
    with open(fn) as fp:
        data_new = json.load(fp)

    data.update(data_new)

    return data

"""
class Settings():
    def __init__(self, fn=None):
        self.load_default()

        #Currently only reads JSON file
        if fn is not None:
            self.load_json(fn)

    def load_default(self):
        '''Load the default settings. Uses the settings_default.json file in the current
        directory
        '''

        self.load_json('settings_default.json')
           
        #Just basing this off of what was originally in this code
        try: 
            if self.BASE_DIR is None:
                self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        except:
            self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def load_json(self, fn):
        '''Update the settings based on an input JSON file

        Params
        ------
        fn : str
            filename for the JSON file
        '''

        with open(fn) as fp:
            settings = json.load(fp)

        #Settings value will only change from default values
        #if they exist in the JSON file
        if 'base_dir' in settings:
            self.BASE_DIR = settings['base_dir']
        if 'normalize_flats' in settings:
            self.NORMALIZE_FLATS = settings['normalize_flats']
        if 'fits_image_hdu' in settings:
            self.FITS_IMAGE_HDU = settings['fits_image_hdu']
        if 'orders' in settings:
            self.ORDERS = settings['orders']
        if 'arcs' in settings:
            self.ARCS = settings['arcs']
        if 'orders_rimas' in settings:
            self.ORDERS_RIMAS = settings['orders_rimas']

    def load_xml(self, fn):
        pass

    def load_txt(self, fn):
        pass

settings = Settings()
"""

settings = load_default()

if __name__ == '__main__':
    #print("settings:", settings.BASE_DIR)
    #print("arcs:", settings.ARCS[0]['element'])
    print("settings:", settings['base_dir'])
    print("arcs:", settings['arcs'][0]['element'])
