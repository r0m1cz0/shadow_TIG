import pyautogui
import time
import webbrowser
import subprocess

def get_mouse_device_id():
    result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    
    for line in lines:
        if 'mouse' in line.lower():
            parts = line.split()
            for part in parts:
                if 'id=' in part:
                    return part.split('=')[1]
    return None

def disable_mouse(device_id):
    subprocess.run(['xinput', 'disable', device_id], capture_output=True, text=True)

def enable_mouse(device_id):
    subprocess.run(['xinput', 'enable', device_id], capture_output=True, text=True)

def main():
	device_id = get_mouse_device_id()
	if device_id:
		print(f"Disabling mouse with device ID: {device_id}")
		disable_mouse(device_id)
		webbrowser.open('https://profile.intra.42.fr/')
		time.sleep(5)  # Attendre que la page se charge

		# Déplacer la souris à la position de l'élément
		pyautogui.moveTo(68, 1024, duration=3)
		pyautogui.click()

		time.sleep(3)

		pyautogui.moveTo(1792, 804, duration=3)
		pyautogui.click()

		time.sleep(5)
		enable_mouse(device_id)
	else:
		print("Mouse device not found.")
	


if __name__ == "__main__":
    main()
