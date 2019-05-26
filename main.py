#!/usr/bin/env python3.6

from windows.app import App
import gettext
import sys

files = dict()
params = sys.argv
is_dev = True
if len(params) > 1:
    if params[1] == 'prod':
        is_dev = False
APP_NAME = "supmti-texteditor"
APP_DIR = "./locales" if is_dev else "/usr/share/locale"

print(APP_DIR)
gettext.bindtextdomain(APP_NAME, APP_DIR)
gettext.textdomain(APP_NAME)
g = gettext.gettext

if __name__ == '__main__':
    main = App(files, is_dev)
    main.main()
