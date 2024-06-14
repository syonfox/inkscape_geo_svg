
import json

#!/usr/bin/env python


import sys

import random
import math
from functools import cached_property

from lxml import etree

# prefix="geo"
# nsuri = "http;//sgol.pub/geosvg"
# inkex.NSS[prefix] = nsuri
# # inkex.utils.NSS[prefix] = nsuri
# inkex.utils.SSN[nsuri] = prefix
# etree.register_namespace(prefix, nsuri)
import sys
import pkgutil
import inkex
from inkex.command import inkscape

# inkex.elements._utils.registerNS("geo2", "http;//sgol.pub/geosvg2")
def dump_object(obj):
    for attribute in dir(obj):
        try:
            value = getattr(obj, attribute)
            inkex.utils.debug(f"{attribute}: {value}")
        except AttributeError:
            inkex.utils.debug(f"{attribute}: Attribute not accessible")



def list_context_and_modules():
    # Dump Python version
    python_version = sys.version
    inkex.utils.debug(f"Python Version: {python_version}")

    # List global modules
    inkex.utils.debug("Global Modules:")
    available_modules = [module_info.name for module_info in pkgutil.iter_modules()]
    for module_name in available_modules:
        inkex.utils.debug(f"Module: {module_name}")

    # List global context
    inkex.utils.debug("Global Context:")
    global_context = globals()
    for name, value in global_context.items():
        inkex.utils.debug(f"Global Variable: {name} = {value}")

    # List built-in functions and variables
    inkex.utils.debug("Built-in Functions and Variables:")
    builtins = __builtins__.__dict__
    for name, value in builtins.items():
        inkex.utils.debug(f"Built-in: {name} = {value}")

    return available_modules


def import_and_dump_modules(whitelisted_modules):
    # Import and dump whitelisted modules
    for module_name in whitelisted_modules:
        inkex.utils.debug(f"Processing module: {module_name}")
        try:
            module = __import__(module_name)
            dump_object(module)
        except ImportError:
            inkex.utils.debug(f"Failed to import module: {module_name}")

# dump_object(inkex)
#
# dump_object(inkex.utils)

class GeoSVGDump(inkex.EffectExtension):

    def __init__(self):
        inkex.Effect.__init__(self)


    def log(self, str):
        self.debug(str)

    def debug_selected_elements(self):
        """Print debug information for each selected element."""
        selected_ids = self.svg.selected
        if not selected_ids:
            self.debug("No objects selected.")
            return

        for element_id in selected_ids:
            element = self.svg.getElement(element_id)
            if element is not None:
                self.debug("El found")
                # print(f"Selected element ID: {element_id}, Tag: {element.tag}, Attributes: {element.attrib}")




    def effect(self):
        python_version = sys.version

        inkex.utils.debug(f"Python Version: {python_version}")


        self.log("Self:")
        dump_object(self)

        self.log("inkex: ")
        dump_object(inkex)

        self.log("etree: ")
        dump_object(etree)

        self.log("inkex.command.inkscape: ")
        dump_object(inkscape)



        self.log("Python Info: ")

        # List available modules and context
        available_modules = list_context_and_modules()

        # Define a whitelist of modules to import and dump
        whitelisted_modules = ['os', 'sys', 're', 'inkex']

        # Import and dump the whitelisted modules
        import_and_dump_modules(whitelisted_modules)
        # dump_python_info()
        self.clean_up()


if __name__ == '__main__':
    e = GeoSVGDump()
    e.run()
