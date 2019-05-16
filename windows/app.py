#!/usr/bin/env python3
import webbrowser

from windows import Gtk, GdkPixbuf, g
from dialogs.about import About
from dialogs.open_file import OpenFile
from widgets.text_view import TextView


class App:
    def destroy(self, widget):
        Gtk.main_quit()

    def about(self, widget):
        About()

    def search(self, widget):
        print("search")

    def save(self, widget):
        is_saved, filename = self.open_file_inst.save()
        if is_saved:
            self.bar.push(0, filename)
        else:
            self.err_dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, g("Alert"))
            self.err_dialog.format_secondary_text("File %s not saved." % filename)
            self.err_dialog.run()

    def open_file(self, widget):
        is_opened, filename = self.open_file_inst.run()
        if is_opened:
            self.bar.push(0, filename)

    def translation(self, widget):
        webbrowser.open("https://www.transifex.com/projects/p/planksetting")

    def report(self, widget):
        webbrowser.open("https://github.com/karim88/SupMTI-TextEditor/issues")

    def __init__(self, files):
        self.files = files
        self.win = Gtk.Window()
        self.win.set_default_size(800, 600)

        # HeadBar
        self.head = Gtk.HeaderBar()
        self.head.props.show_close_button = True
        self.head.props.title = g("SupMTI-TextEditor")
        self.win.set_titlebar(self.head)

        # Containers
        self.box = Gtk.VBox()
        self.menu = Gtk.MenuBar()
        self.menu.set_hexpand(True)

        # Text Editor
        self.textview = TextView(self.files)
        self.open_file_inst = OpenFile(self.files, self.textview)

        # StatusBar
        self.bar = Gtk.Statusbar()
        self.bar.push(0, g("New file"))

        self.stmenu = Gtk.MenuItem(g("Menu"))
        self.menu.append(self.stmenu)
        self.m = Gtk.Menu()
        self.stmenu.set_submenu(self.m)
        """ Open file """
        self.open = Gtk.MenuItem(g("Open file"))
        self.open.connect('activate', self.open_file)
        self.m.append(self.open)
        """ Save """
        self.save_widget = Gtk.MenuItem(g("Save"))
        self.save_widget.connect('activate', self.save)
        self.m.append(self.save_widget)
        """ Translate """
        self.tra = Gtk.MenuItem(g("Translate this Application"))
        self.tra.connect('activate', self.translation)
        self.m.append(self.tra)
        """ Report a bug """
        self.bug = Gtk.MenuItem(g("Report a bug"))
        self.bug.connect('activate', self.report)
        self.m.append(self.bug)
        """ About """
        self.abt = Gtk.MenuItem(g("About"))
        self.abt.connect('activate', self.about)
        self.m.append(self.abt)
        """ Exit """
        self.xit = Gtk.MenuItem(g("Exit"))
        self.xit.connect('activate', self.destroy)
        self.m.append(self.xit)

        """ Search """

        self.search_menu = Gtk.ImageMenuItem(Gtk.STOCK_NEW)
        self.menu.append(self.search_menu)
        self.search_menu.connect('activate', self.search)

        self.head.pack_start(self.menu)
        self.box.pack_end(self.bar, False, False, 0)
        self.box.pack_end(self.textview.scrolled_window, True, True, 0)

        self.win.add(self.box)
        self.win.show_all()
        self.win.connect("destroy", self.destroy)

    def main(self):
        Gtk.main()
