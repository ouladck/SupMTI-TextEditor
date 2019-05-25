from widgets import Gtk, GtkSource, g

class OpenFile:
    """docstring for OpenFile."""

    def __init__(self, files, textview):
        self.files = files
        self.textview = textview

    def run(self):
        filename = ''
        self.dialog = Gtk.FileChooserDialog(g("Please choose a file"), None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.response = self.dialog.run()
        if self.response == Gtk.ResponseType.OK:
            filename = self.dialog.get_filename()
            with open(self.dialog.get_filename(), 'r+') as file:
                self.read_file(filename, file)
            self.dialog.destroy()
            return [True, filename]

        elif self.response == Gtk.ResponseType.CANCEL:
            self.dialog.destroy()
            return [False, filename]

        return [False, g('New file (err)')]

    def get_files(self):
        return self.files

    def read_file(self, filename, file):
        self.files[filename] = ''.join(file.readlines())
        self.textview.textbuffer.set_text(self.files[filename])
        guessed_language = self.textview.lang_manager.guess_language(filename)
        self.textview.textbuffer.set_language(guessed_language)

    def save(self):
        filename = ''
        self.save_dialog = Gtk.FileChooserDialog(g("Please choose a file"), None,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.save_dialog.set_do_overwrite_confirmation(True)
        content = self.textview.textbuffer.get_text(
            self.textview.textbuffer.get_start_iter(),
            self.textview.textbuffer.get_end_iter(), True)

        self.save_response = self.save_dialog.run()
        if self.save_response == Gtk.ResponseType.OK:
            filename = self.save_dialog.get_filename()
            with open(filename, 'w+') as file:
                file.writelines(content)
            self.save_dialog.destroy()
            return [True, filename]

        elif self.save_response == Gtk.ResponseType.CANCEL:
            self.save_dialog.destroy()
            return [False, filename]

        return [False, '']
