from window_lib import *
from scanner_lib import openvas_start
import platform

if platform.system() == 'Linux':
    openvas_start.start()
app = MyApp()
app.MainLoop()
