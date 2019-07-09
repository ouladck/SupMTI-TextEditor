from widgets import Gtk, GtkSource
from dialogs.search import Search
from dialogs.replace import Replace


class TextView:

    def __init__(self, files):
        self.files = files
        self.found = []
        self.tmp_found = []
        self.match_start = None
        self.match_end = None
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.show()

        self.text_view = GtkSource.View()
        self.text_view.set_show_line_numbers(True)
        self.text_view.set_highlight_current_line(True)
        self.text_view.set_auto_indent(True)
        self.text_view.set_background_pattern(GtkSource.BackgroundPatternType.GRID)
        self.text_view.set_cursor_visible(True)
        self.text_view.set_left_margin(2)
        self.text_view.set_right_margin(2)

        self.textbuffer = GtkSource.Buffer()
        self.lang_manager = GtkSource.LanguageManager()
        self.textbuffer.set_highlight_syntax(True)
        self.textbuffer.set_highlight_matching_brackets(True)
        self.textbuffer.set_text("print('Hello SupMTI')")
        self.text_view.set_buffer(self.textbuffer)
        self.textbuffer.set_language(self.lang_manager.get_language('python'))
        self.scrolled_window.add_with_viewport(self.text_view)
        self.tag_found = self.textbuffer.create_tag("found", background="yellow")

        self.text_view.show()

    def test_dialog_response(self, dialog, is_search):
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cursor_mark = self.textbuffer.get_insert()
            start = self.textbuffer.get_iter_at_mark(cursor_mark)
            if start.get_offset() == self.textbuffer.get_char_count():
                start = self.textbuffer.get_start_iter()

            if is_search:
                self.search_and_mark(dialog.entry.get_text(), start)
            else:
                replaced_text = self.textbuffer.get_text(
                    self.textbuffer.get_start_iter(),
                    self.textbuffer.get_end_iter(),
                    True
                ).replace(
                    dialog.entry.get_text(),
                    dialog.replace.get_text()
                )
                self.textbuffer.set_text(replaced_text)

    def on_search_clicked(self):
        dialog = Search()

        self.test_dialog_response(dialog, True)

        dialog.destroy()

    def on_replace_clicked(self):
        dialog = Replace()
        self.test_dialog_response(dialog, False)
        dialog.destroy()

    def search_and_mark(self, text, start):
        end = self.textbuffer.get_end_iter()
        match = start.forward_search(text, 0, end)

        if match is not None:
            self.tmp_found.append(match)
            self.match_start, self.match_end = match
            self.textbuffer.apply_tag(self.tag_found, self.match_start, self.match_end)
            self.search_and_mark(text, self.match_end)
        else:
            self.found = self.tmp_found

    def on_clear_clicked(self):
        start = self.textbuffer.get_start_iter()
        end = self.textbuffer.get_end_iter()
        self.textbuffer.remove_tag(self.tag_found, start, end)
