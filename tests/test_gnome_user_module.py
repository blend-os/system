from user_modules.gnome import call


def test_config_setting_gtk_theme():
    assert call({"gtk-theme": 'adw-gtk3'}) == {
        "commands": [
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'gtk-theme', 'adw-gtk3']
        ]
    }


def test_config_setting_icon_theme():
    assert call({"icon-theme": 'Adwaita'}) == {
        "commands": [
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'icon-theme', 'Adwaita']
        ]
    }


def test_config_setting_style():
    assert call({"style": "light"}) == {
        "commands": [
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'color-scheme', 'prefer-light']
        ]
    }


def test_config_titlebar():

    assert call({
        "titlebar": {
            "button-placement": "right",
            "double-click-action": "toggle-maximize",
            "middle-click-action": "minimize",
            "right-click-action": "menu"
        }
    }) == {
        "commands": [
            ['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'button-layout', 'appmenu:minimize,maximize,close'],
            ['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-double-click-titlebar', "toggle-maximize"],
            ['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-middle-click-titlebar', "minimize"],
            ['gsettings', 'set', 'org.gnome.desktop.wm.preferences', 'action-right-click-titlebar', "menu"]
        ]
    }