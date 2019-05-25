#!/usr/bin/env python3.6

from windows.app import App
import gettext

files = dict()
APP_NAME = "supmti-texteditor"
APP_DIR = "./locales"
gettext.bindtextdomain(APP_NAME, APP_DIR)
gettext.textdomain(APP_NAME)
g = gettext.gettext

if __name__ == '__main__':
    main = App(files)
    main.main()
