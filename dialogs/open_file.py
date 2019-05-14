from widgets import Gtk, GtkSource

class OpenFile:
    """docstring for OpenFile."""

    def __init__(self, files, textview):
        self.files = files
        self.textview = textview
        self.dialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        # self.add_filters(dialog)

    def run(self):
        self.response = self.dialog.run()
        if self.response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + self.dialog.get_filename())
            with open(self.dialog.get_filename(), 'r+') as file:
                self.read_file(self.dialog.get_filename(), file)

        elif self.response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        self.dialog.destroy()

    def get_files(self):
        return self.files

    def read_file(self, filename, file):
        self.files[filename] = ''.join(file.readlines())
        self.textview.textbuffer.set_text(self.files[filename])
        guessed_language = self.textview.lang_manager.guess_language(filename)
        self.textview.textbuffer.set_language(guessed_language)

    def save(self):
        print(self.textview.textbuffer.get_text(
            self.textview.textbuffer.get_start_iter(),
            self.textview.textbuffer.get_end_iter(), True))
