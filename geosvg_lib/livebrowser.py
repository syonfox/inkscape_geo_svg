import os
import time
import webbrowser

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
        print("Stopped monitoring.")

# Usage example:
# live_reload('/path/to/your/file.html')
