'''A module for handling GNOME tweaks.'''


def call(config):
    return_val = {
        'commands': []
    }

    if type(config.get('gtk-theme')) == str:
        return_val['commands'].append(
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'gtk-theme', config.get('gtk-theme')])

    if type(config.get('icon-theme')) == str:
        return_val['commands'].append(
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'icon-theme', config.get('gtk-theme')])

    if type(config.get('style')) == str:
        return_val['commands'].append(
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'color-scheme', 'prefer-' + config.get('style')])

    if type(config.get('titlebar')) == dict:
        if type(config['titlebar'].get('button-placement')) == str:
            return_val['commands'].append(['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'button-layout', [
                                          'minimize,maximize,close:appmenu', 'appmenu:minimize,maximize,close'][config['titlebar'].get('button-placement') == 'right']])

        if type(config['titlebar'].get('double-click-action')) == str:
            return_val['commands'].append(['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-double-click-titlebar', config['titlebar'].get('double-click-action')])

        if type(config['titlebar'].get('middle-click-action')) == str:
            return_val['commands'].append(['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-middle-click-titlebar', config['titlebar'].get('middle-click-action')])

        if type(config['titlebar'].get('right-click-action')) == str:
            return_val['commands'].append(['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-right-click-titlebar', config['titlebar'].get('right-click-action')])

    return return_val
