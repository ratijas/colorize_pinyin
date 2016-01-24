# -*- coding: UTF-8 -*-
# Copyleft 2016 Ratijas <ratijas.t@me.com>
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

from __future__ import print_function
import sys

import colorize_pinyin


def usage():
    print('usage:')
    print('\t%s [--] "string with chinese pinyin"' % sys.argv[0])
    print('\t%s [-h | --help]  # display this help' % sys.argv[0])
    print('\t%s -v | --version  # print version' % sys.argv[0])
    print('')
    print('prints colorized HTML string to stdout.')
    print('if no pinyin found, prints nothing and exits with code 2')
    return 1


def version():
    print(colorize_pinyin.__version__)
    return 0


def _main():
    if not sys.argv[1:]:
        return 2
    line = ' '.join(sys.argv[1:])
    colored = colorize_pinyin.colorized_HTML_string_from_string(line)
    if not colored:
        return 2
    print(colored)
    return 0


def main():
    if not sys.argv[1:]:
        return usage()
    if sys.argv[1] in ('-h', '--help'):
        usage()
        return 0
    if sys.argv[1] in ('-v', '--version'):
        return version()
    if sys.argv[1] == '--':
        del sys.argv[1]
    return _main()


if __name__ == '__main__':
    sys.argv[0] = 'python -m colorize_pinyin'
    exit(main())
