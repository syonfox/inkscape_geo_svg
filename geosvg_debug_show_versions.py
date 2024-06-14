#!/usr/bin/env python3
import sys
import os
import inkex
import subprocess
import pkgutil

# from inkex.command

# Add the subdirectory to the system path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'geosvg_lib'))

# Now you can import the module
# import inkexcmd
from geosvg_lib import inkexcmd
# import psutil

def get_python_version():
    return sys.version

def get_os_version():
    return os.uname() if hasattr(os, 'uname') else os.name

# def get_inkscape_version():
#     try:
#         result = subprocess.run(['inkscape', '--version'], stdout=subprocess.PIPE)
#         version_info = result.stdout.decode('utf-8').strip()
#         return version_info
#     except Exception as e:
#         return f"Error retrieving Inkscape version: {e}"
# import inkex.command as inkscape

# INKSCAPE_EXECUTABLE_NAME = os.environ.get("INKSCAPE_COMMAND")

# def get_inkscape_version(svg):
#     # The command to get the Inkscape version
#     command = '--version'
#
#     # inkex.debug(command)
#     # Call Inkscape with the command
#     result = inkex.command.call_inkscape(svg, command)
#
#     # Return the result
#     return result


def get_inkscape_version(self):
    try:
        # Use the call function to execute the --version command
        version_info = inkexcmd.call(inkexcmd.INKSCAPE_EXECUTABLE_NAME, '--version')
        return version_info
    except inkex.command.ProgramRunError as e:
        return f"An error occurred: {e}"

# def get_inkscape_version2():
#         try:
#             # Get the parent process (Inkscape)
#             parent_process = psutil.Process(os.getppid())
#             if 'inkscape' in parent_process.name().lower():
#                 version_info = parent_process.cmdline()
#                 return ' '.join(version_info)
#             else:
#                 return "Inkscape version could not be detected from the parent process"
#         except Exception as e:
#             return f"Error retrieving Inkscape version: {e}"

def get_inkex_version():
    try:
        return inkex.__version__
    except AttributeError:
        return "1.0"

# def get_process_tree():
#     try:
#         # Get the current process
#         current_process = psutil.Process()
#         # Traverse the process tree upwards
#         tree = []
#         while current_process:
#             tree.append(f"{current_process.pid} - {current_process.name()}")
#             if current_process.pid == 1:
#                 break
#             current_process = current_process.parent()
#         return " > ".join(tree[::-1])
#     except Exception as e:
#         return f"Error retrieving process tree: {e}"

def list_available_modules():
    return [module_info.name for module_info in pkgutil.iter_modules()]

def detect(self):
    detection_info = {
        "python_version": get_python_version(),
        "os_version": get_os_version(),


        "inkscape_version": get_inkscape_version(self.svg),
        "inkscape_available: ": inkexcmd.is_inkscape_available(),
        # "inkscape_version2":get_inkscape_version2(),
        "inkex_version": get_inkex_version(),
        "available_modules": list_available_modules(),
        # "process_tree": get_process_tree()
    }

    return detection_info

class GeoSVGDumper(inkex.Effect):
    def __init__(self):
        super().__init__()

    def effect(self):
        detection_info = detect(self)
        for key, value in detection_info.items():
            if key == "available_modules":
                self.log(f"{key}: {', '.join(value)}")
            else:
                self.log(f"{key}: {value}")

    def log(self, msg):
        self.debug(msg)

if __name__ == "__main__":
    e = GeoSVGDumper()
    e.run()
