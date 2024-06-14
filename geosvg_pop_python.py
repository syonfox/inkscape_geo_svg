import os
import sys
import subprocess
import tempfile
import inkex
from lxml import etree

class MyPythonShellPlugin(inkex.EffectExtension):
    def effect(self):
        # Gather context information
        context_info = {
            'document_width': self.svg.width,
            'document_height': self.svg.height,
            'svg_content': etree.tostring(self.document, encoding='unicode')
        }

        # Create a temporary file to store the context
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.py') as tmpfile:
            # tmpfile.write("import inkex\n")
            tmpfile.write(f"context_info = {context_info}\n")
            tmpfile.write("""
# import code
help_text = '''
Inkscape Python Shell:
- context_info: A dictionary containing document width, height, and SVG content.
'''
print("Hellow World")
print(help_text)
# code.interact(local=locals())
input('Press Enter to exit the shell...')  # Keeps the terminal open
            """)
            tmpfile_path = tmpfile.name

        # Determine the terminal command based on the operating system
        if sys.platform == "win32":
            # On Windows, use cmd.exe to start a new command prompt
            terminal_command = ['cmd.exe', '/c', 'start', 'python', tmpfile_path]
            creationflags = subprocess.CREATE_NEW_CONSOLE
            process = subprocess.Popen(terminal_command, creationflags=creationflags)
        elif sys.platform == "darwin":
            # On macOS, use open -a Terminal.app to open a new terminal window
            terminal_command = ['open', '-a', 'Terminal.app', 'python3', tmpfile_path]
            process = subprocess.Popen(terminal_command)
        else:
            tmpdir = "/tmp"
            # On Linux, use x-terminal-emulator to open the default terminal
            # terminal_command = ['x-terminal-emulator', '-e', f'bash -c "python3 {tmpfile_path}; read -p \'Press Enter to exit the shell...\';"']
            terminal_command = ['x-terminal-emulator', '-e', f'bash -c "cd {tmpdir} && python3 context_script.py; exec bash"']
            process = subprocess.Popen(terminal_command, preexec_fn=os.setsid)

        # Wait for the terminal process to exit
        process.wait()

if __name__ == '__main__':
    MyPythonShellPlugin().run()
