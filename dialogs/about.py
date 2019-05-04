from dialogs import Gtk, GdkPixbuf, g


class About:
    def __init__(self):
        about = Gtk.AboutDialog()
        about.set_program_name(g("SupMTI-TextEditor"))
        about.set_logo(
            GdkPixbuf
                .Pixbuf.new_from_file("/usr/share/pixmaps/planksetting.png"))
        about.set_icon(
            GdkPixbuf.Pixbuf
                .new_from_file("/usr/share/pixmaps/planksetting_logo.png"))
        about.set_version("0.1.4.1")
        about.set_comments(
            g("A stupid application to customize plank dock easily."))
        about.set_copyright("Copyright (c) 2014-2017 Karim Oulad Chalha")
        about.set_website("http://karim88.github.io/PlankSetting/")
        about.set_website_label(g("PlankSetting website"))
        about.set_authors(["Karim Oulad Chalha"])
        about.set_license(g("GPL v3"))
        about.set_translator_credits(g("translator-credits"))

        about.run()
        about.destroy()