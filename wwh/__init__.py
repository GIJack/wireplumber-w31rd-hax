#!/usr/bin/env python3
'''
wwh - Wireplumber W31rd Hax

Common python library for GUI and CLI
'''

import os

class _lib_meta:
    lib_ver = "0.1.0"

class default_var:
    config_dirs            = ['/usr/share/wireplumber-w31rd-hax','/usr/local/share/wireplumber-w31rd-hax']
    wireplumber_config_dir = "%s/.config/wireplumber/wireplumber.conf.d/" % os.getenv("HOME")
