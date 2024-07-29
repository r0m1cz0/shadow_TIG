import webview
import platform
from Xlib import display, X
from Xlib.ext import randr

# Chemin vers le fichier HTML
html_file = 'static/index.html'

def disable_close(window):
    if platform.system() == 'Linux':
        d = display.Display()
        root = d.screen().root
        window_id = root.get_full_property(d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType).value[0]
        window = d.create_resource_object('window', window_id)

        # Mask for properties we are interested in
        WM_HINTS = d.intern_atom('_MOTIF_WM_HINTS')

        # Create the property data structure
        hints = window.get_property(WM_HINTS, X.AnyPropertyType, 0, 32).value
        hints = hints[:2] + (hints[2] | 1, ) + hints[3:]  # Set the third element to 1 (disable close)

        # Change the property
        window.change_property(WM_HINTS, X.AnyPropertyType, 32, hints)

        # Flush the display to make sure the changes take effect
        d.flush()

if __name__ == '__main__':
    # Créer la fenêtre
    window = webview.create_window('My Webview App', html_file, fullscreen=True)

    # Démarrer l'application avec la fonction de blocage
    webview.start(func=disable_close, args=(window,))
