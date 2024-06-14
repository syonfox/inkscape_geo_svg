import os
import subprocess
import time
import webbrowser
import sys

def live_reload(file_path):
    # Open the file in Firefox
    webbrowser.get('firefox').open_new_tab(file_path)

    # Get the initial modification time
    last_mod_time = os.path.getmtime(file_path)

    try:
        while True:
            time.sleep(1)  # Check every second
            current_mod_time = os.path.getmtime(file_path)

            if current_mod_time != last_mod_time:
                last_mod_time = current_mod_time
                # Reload the file in Firefox
                webbrowser.get('firefox').open_new_tab(file_path)

    except KeyboardInterrupt:
        pass  # Handle any cleanup if necessary


def open_in_editor(file_path, editor='featherpad'):
    editors = ['featherpad', 'nano', 'vi']
    if editor not in editors:
        editor = editors[0]  # Default to featherpad

    subprocess.Popen([editor, file_path])

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.exit("Usage: live_reload_script.py <file_path> [editor]")

    file_path = sys.argv[1]
    editor = sys.argv[2] if len(sys.argv) == 3 else 'featherpad'

    if os.path.isfile(file_path):
        open_in_editor(file_path, editor)
        live_reload(file_path)
    else:
        sys.exit("Invalid file path")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: live_reload_script.py <file_path>")

    file_path = sys.argv[1]
    if os.path.isfile(file_path):
        live_reload(file_path)
        open_in_editor(file_path)
    else:
        sys.exit("Invalid file path")
