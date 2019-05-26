#!/usr/bin/env python3
import webbrowser

from dialogs.search import Search
from windows import Gtk, Gdk, g
from dialogs.about import About
from dialogs.open_file import OpenFile
from widgets.text_view import TextView


class App:
    def destroy(self, widget):
        Gtk.main_quit()

    def about(self, widget):
        About(self.is_dev)

    def search(self, widget):
        self.textview.on_clear_clicked()
        self.textview.on_search_clicked()

    def replace(self, widget):
        self.textview.on_clear_clicked()
        self.textview.on_replace_clicked()

    def save(self, widget):
        is_saved, filename = self.open_file_inst.save()
        if is_saved:
            self.bar.push(0, filename)
        else:
            self.err_dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, g("Alert"))
            self.err_dialog.format_secondary_text(g("File %s not saved.") % filename)
            self.err_dialog.show()

    def save_as(self, widget):
        is_saved, filename = self.open_file_inst.save_as()
        if is_saved:
            self.bar.push(0, filename)
        else:
            self.err_dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, g("Alert"))
            self.err_dialog.format_secondary_text(g("File %s not saved.") % filename)
            self.err_dialog.show()

    def open_file(self, widget):
        is_opened, filename = self.open_file_inst.run()
        if is_opened:
            self.bar.push(0, filename)

    def _key_press_event(self, widget, event):
        keyval = event.keyval
        keyval_name = Gdk.keyval_name(keyval)
        state = event.state
        ctrl = (state & Gdk.ModifierType.CONTROL_MASK)
        if ctrl and keyval_name == 's':
            self.save(widget)
        elif ctrl and keyval_name == 'o':
            self.open_file(widget)
        elif ctrl and keyval_name == 'q':
            self.destroy(widget)
        elif ctrl and keyval_name == 'r':
            self.replace(widget)
        elif ctrl and keyval_name == 'f':
            self.search(widget)
        elif keyval_name == "Escape":
            self.destroy(widget)
        else:
            return False
        return True

    def translation(self, widget):
        webbrowser.open("https://github.com/karim88/SupMTI-TextEditor")

    def report(self, widget):
        webbrowser.open("https://github.com/karim88/SupMTI-TextEditor/issues")

    def __init__(self, files, is_dev):
        self.is_dev = is_dev
        self.files = files
        self.win = Gtk.Window()
        self.win.set_default_size(800, 600)

        self.win.connect('key-press-event', self._key_press_event)

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
        """ Save as """
        self.save_widget = Gtk.MenuItem(g("Save as"))
        self.save_widget.connect('activate', self.save_as)
        self.m.append(self.save_widget)
        """ Search """
        self.search_menu = Gtk.MenuItem(g('Find'))
        self.m.append(self.search_menu)
        self.search_menu.connect('activate', self.search)
        """ Search & Eeplace """
        self.replace_menu = Gtk.MenuItem(g('Find & Replace'))
        self.m.append(self.replace_menu)
        self.replace_menu.connect('activate', self.replace)
        """ Exit """
        self.xit = Gtk.MenuItem(g("Exit"))
        self.xit.connect('activate', self.destroy)
        self.m.append(self.xit)

        self.hmenu = Gtk.MenuItem(g("Help"))
        self.menu.append(self.hmenu)
        self.m2 = Gtk.Menu()
        self.hmenu.set_submenu(self.m2)
        """ Translate """
        self.tra = Gtk.MenuItem(g("Translate this Application"))
        self.tra.connect('activate', self.translation)
        self.m2.append(self.tra)
        """ Report a bug """
        self.bug = Gtk.MenuItem(g("Report a bug"))
        self.bug.connect('activate', self.report)
        self.m2.append(self.bug)
        """ About """
        self.abt = Gtk.MenuItem(g("About"))
        self.abt.connect('activate', self.about)
        self.m2.append(self.abt)

        self.head.pack_start(self.menu)
        self.box.pack_end(self.bar, False, False, 0)
        self.box.pack_end(self.textview.scrolled_window, True, True, 0)

        self.win.add(self.box)
        self.win.show_all()
        self.win.connect("destroy", self.destroy)

    def main(self):
        Gtk.main()
