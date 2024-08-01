#!/bin/bash

user=$(whoami)
search_url="https://profile.intra.42.fr/users/{user}"
# Effectuer la recherche sur le site web
curl "$search_url"

# tkt faut vériff en gros sa telecharge la page puis en extrait l'image.
page_content=$(curl -s "$search_url")

# Extraire l'URL de la première image (adapté pour une balise <img>)
image_url=$(echo "$page_content" | grep -oP '(?<=<img src=")[^"]+' | head -n 1)

# Vérifier si une image a été trouvée
if [ -z "$image_url" ]; then
    echo "No image found on the page."
    exit 1
fi

echo "Image URL found: $image_url"

# Télécharger l'image dans le répertoire d'exécution
image_name=$(basename "$image_url")
curl -o "$image_name" "$image_url"

echo "Image downloaded as $image_name"