import os
import json

def load_default():
    '''Load the default settings'''
    local_dirname = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(local_dirname, 'settings_default.json')
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

settings_default = load_default()

if __name__ == '__main__':
    print("settings:", settings_default['base_dir'])
    print("arcs:", settings_default['arcs'][0]['element'])
