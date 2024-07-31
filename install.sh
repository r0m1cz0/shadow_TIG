#!/bin/bash

# Fonction pour ouvrir un terminal et exécuter une commande
open_terminal_with_command() {
	commands="curl parrot.live; sleep 10; kill; cat ./install/troll.txt exec bash"
	gnome-terminal -- bash -c "$1; $2; $3; $4; exec bash"
}

open_terminal_with_command
# Installer les modules nécessaires
pip install pyautogui -qqq
pip install pywebview -qqq
pip install Xlib -qqq
# Ouvrir un terminal et exécuter la commande curl

