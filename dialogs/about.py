from dialogs import Gtk, GdkPixbuf, g


class About:
    def __init__(self, is_dev):
        image = "./assets/supmti.png" if is_dev else "/usr/share/pixmaps/supmti.png"
        license = "./LICENSE" if is_dev else "/usr/share/SupMTI-TextEditor/LICENSE"
        about = Gtk.AboutDialog()
        about.set_program_name(g("SupMTI-TextEditor"))
        about.set_logo(
            GdkPixbuf
                .Pixbuf.new_from_file(image))
        about.set_icon(
            GdkPixbuf.Pixbuf
                .new_from_file(image))
        about.set_version("1.2.1")
        about.set_comments(
            g("A stupid Text Editor make with PyGTK.\nIt's a part of my Python Min-project for SupMTI Rabat."))
        about.set_copyright(g("Copyright (c) 2019 Karim Oulad Chalha"))
        about.set_website("https://github.com/karim88/SupMTI-TextEditor")
        about.set_website_label(g("Github repo."))
        about.set_authors(["Karim Oulad Chalha"])
        with open(license, 'r') as license_file:
            license_text = ''.join(license_file.readlines())
            about.set_license(license_text)
        about.set_translator_credits(g("translator-credits"))

        about.run()
        about.destroy()