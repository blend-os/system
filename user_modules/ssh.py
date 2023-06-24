'''A module for handling SSH configuration.'''


def call(config):
    return_val = {
        'files': {}
    }

    if type(config.get('allowed_keys')) == list:
        authorized_keys = ''
        for key in config.get('allowed_keys'):
            if type(key) == str:
                authorized_keys += key + '\n'
        return_val['files']['.ssh/authorized_keys'] = authorized_keys
    
    return return_val