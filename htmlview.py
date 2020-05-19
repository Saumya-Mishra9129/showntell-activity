import os

from gi.repository import Gtk
from gi.repository.WebKit2 import WebView

from sugar3 import env
from sugar3.activity import activity
##hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))

BUNDLEPATH = os.path.join(activity.get_bundle_path() , 'tw')
DATAPATH = os.path.join(activity.get_activity_root() , 'data')
TESTFILE = BUNDLEPATH + 'slides.html'
WORKFILE = 'file://' + DATAPATH + 'slides.html'


class Htmlview(Gtk.VBox):

    def __init__(self):
        Gtk.VBox.__init__(self)
        self.set_spacing(8)

        wv = WebView()
        print(('show', WORKFILE, os.path(WORKFILE).exists()))
        wv.load_uri(WORKFILE)
        wv.show()
        self.pack_start(wv, True, True, 0)
        # self.add(wv)
        self.show_all()
