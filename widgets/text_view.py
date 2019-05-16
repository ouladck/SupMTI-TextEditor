from widgets import Gtk, GtkSource
from dialogs.search import Search


class TextView:

    def __init__(self, files):
        self.files = files
        print('tEXTvIEW')
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

        self.text_view.show()


    def on_search_clicked(self, widget):
        dialog = Search(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cursor_mark = self.textbuffer.get_insert()
            start = self.textbuffer.get_iter_at_mark(cursor_mark)
            if start.get_offset() == self.textbuffer.get_char_count():
                start = self.textbuffer.get_start_iter()

            self.search_and_mark(dialog.entry.get_text(), start)

        dialog.destroy()

    def search_and_mark(self, text, start):
        end = self.textbuffer.get_end_iter()
        match = start.forward_search(text, 0, end)

        if match is not None:
            match_start, match_end = match
            self.textbuffer.apply_tag(self.tag_found, match_start, match_end)
            self.search_and_mark(text, match_end)
