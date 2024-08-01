import pyautogui
import time

def move_mouse_alternating():
    """Move the mouse cursor between the original spot and a new position every minute."""
    original_position = pyautogui.position()
    alternate_position = (original_position[0] + 10, original_position[1] + 10)  # Adjust the values as needed
    toggle = False

    while True:
        if toggle:
            pyautogui.moveTo(original_position)
        else:
            pyautogui.moveTo(alternate_position)
        
        toggle = not toggle
        time.sleep(10)  # Wait for 60 seconds

def main():
    move_mouse_alternating()

if __name__ == "__main__":
    main()