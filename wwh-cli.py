#!/usr/bin/env python3
app_desc='''wwh-cli.py - Wireplumper W31rd Hax
Enable and Disable bundled config files that fix various problems or enact
various effects.

    USAGE:
wwh-cli.py <command> [options]

    COMMANDS:
list    -   List available "hacks" are available, and which of those are enabled

enable  -   Enable a hack, specify the name of the hack

disable -   Disable a hack, specify the name of the hack
'''

from .wwh import *
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description=app_desc,epilog="\n\n",add_help=False,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", nargs="?"   , help="See above for description of commands")
    parser.add_argument("-?", "--help"         , help="Show This Help Message", action="help")
    parser.add_argument("-v","--version"       , help="Print Version and Exit", action="store_true")
    parser.add_argument("-t","--terse"         , help="output as CSV rather than a formatted table, useful for scripts", action="store_true")
    args = parser.parse_args()
    
    if args.version == True:
        message_line = "Wireplumber W13rd Hax VERSION: %s" % (_lib_meta.lib_ver)
        print(message_line)
        sys.exit(4)
    

if __name__ == "__main__":
    main()
