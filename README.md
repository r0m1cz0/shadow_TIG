# shadow_TIG
tkt c'est marrant :D
```bash
curl parrot.live
```


```python
import pyautogui
import time
import webbrowser

# Ouvrir Firefox et aller à une URL définie
webbrowser.open('https://profile.intra.42.fr/')
time.sleep(5)  # Attendre que la page se charge

# Déplacer la souris à la position de l'élément
pyautogui.moveTo(68, 1024, duration=3)
pyautogui.click()

time.sleep(3)

pyautogui.moveTo(1792, 804, duration=3)
pyautogui.click()

```
