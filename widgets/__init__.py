import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Pango
from gi.repository import GdkPixbuf
from gettext import gettext as g

from pygments.lexer import Lexer as PythonLexer
from pygments.styles.colorful import ColorfulStyle