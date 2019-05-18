from dialogs import Gtk, GdkPixbuf, g


class Search(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, g("Search"), parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_FIND, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label(g("Insert text you want to search for:"))
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()