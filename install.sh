#!/bin/bash

# Fonction pour ouvrir un terminal et exécuter une commande
open_terminal_with_command() {

	gnome-terminal -- bash -c "$1; exec bash" #, "$2; exec bash","$3; exec bash","$4; exec bash"
}

# Installer les modules nécessaires
pip install pyautogui -qqq
pip install pywebview -qqq
pip install Xlib -qqq
# Ouvrir un terminal et exécuter la commande curl
open_terminal_with_command "curl parrot.live", "sleep 10", "kill $CURL_PID", "cat ./install/troll.txt"

