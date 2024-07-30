import pyautogui
import time

def move_and_click(x:int=100, y:int=100, duration:int=1) -> None:
    # Déplacer la souris à la position (x, y)
    pyautogui.moveTo(x, y, duration=1)  # duration est le temps en secondes pour le déplacement
    # Cliquer à la position actuelle de la souris
    pyautogui.click()

def main() -> None:
    # Attendre 5 secondes avant de commencer pour vous laisser le temps de préparer
    time.sleep(5)
    
    # Coordonnées où vous voulez déplacer la souris et cliquer
    x = 100
    y = 100
    duration = 1
    
    for i in range(10) :
        move_and_click(x, y, duration)
        x += 100
        y += 50
        time.sleep(1.5)

if __name__ == "__main__":
    main()
