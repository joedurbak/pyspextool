import os
import json

class XSpectreConfig(object):
    """Configuration object for the Xspectre settings. It will be accessed
    like a dictionary"""

    #This is a class in case we want to do something add more functionality
    #than what just a dictionary provides
    def __init__(self, fn=None):
        self.__settdict__ = {}
    
        local_dirname = os.path.dirname(os.path.abspath(__file__))
        fn_def = os.path.join(local_dirname, 'settings_default.json')
        with open(fn_def) as fp:
            self.__settdict__ = json.load(fp)

        self.__settdict__['base_dir'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        if fn is not None:
            self.load_json(fn)

    def __setitem__(self, key, item):
        self.__settdict__[key] = item

    def __getitem__(self, key):
        return self.__settdict__[key]

    def load_config(self, fn):
        # TODO: check suffix of file to determine which load_XXXX method to call
        pass

    def load_json(self, fn):
        '''Load a JSON settings file

        Params
        ------
        fn : str
            Filename of the JSON settings file

        Notes
        -----
        Any settings not in the JSON file are set to their default values
        '''

        with open(fn) as fp:
            data_new = json.load(fp)

        self.__settdict__.update(data_new)

settings_default = XSpectreConfig()

if __name__ == '__main__':
    print("settings:", settings_default['base_dir'])
    print("arcs:", settings_default['arcs'][0]['element'])
