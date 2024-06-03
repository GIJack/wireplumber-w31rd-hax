#!/usr/bin/env python3

'''
Wireplumber W31rd Hax

printing functions: message, warn, exit_with_error
'''

import sys

def warn(message):
    message = "wwh: %s%s¡WARN!:%s %s" % (colors.yellow, colors.bold, colors.reset, message)
    print("wwh:" + colors.yellow + colors.bold + "¡WARN!: " + colors.reset + message, file=sys.stderr)
    return

def message(message):
    print("wwh: " + message)

def exit_with_error(exit,message):
    print("wwh:" + colors.red + colors.bold + " ¡ERROR!: " + colors.reset + message, file=sys.stderr)
    sys.exit(exit)
