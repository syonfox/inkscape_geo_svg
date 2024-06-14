#!/usr/bin/env python3
import os
import subprocess

import inkex
import webbrowser
from geosvg_lib import livebrowser;
def _pythonpath():
    for pth in os.environ.get("PYTHONPATH", "").split(":"):
        if os.path.isdir(pth):
            yield pth

# [docs]
def get_user_directory():
    """Return the user directory where extensions are stored.

    .. versionadded:: 1.1"""
    if "INKSCAPE_PROFILE_DIR" in os.environ:
        return os.path.abspath(
            os.path.expanduser(
                os.path.join(os.environ["INKSCAPE_PROFILE_DIR"], "extensions")
            )
        )

    home = os.path.expanduser("~")
    for pth in _pythonpath():
        if pth.startswith(home):
            return pth
    return None



# [docs]
def get_inkscape_directory():
    """Return the system directory where inkscape's core is.

    .. versionadded:: 1.1"""
    for pth in _pythonpath():
        if os.path.isdir(os.path.join(pth, "inkex")):
            return pth
    raise ValueError("Unable to determine the location of Inkscape")


def dump_object(obj):
    for attribute in dir(obj):
        try:
            value = getattr(obj, attribute)
            inkex.utils.debug(f"{attribute}: {value}")
        except AttributeError:
            inkex.utils.debug(f"{attribute}: Attribute not accessible")



class GeoSVGShowXML(inkex.Effect):
    def __init__(self):
        super().__init__()

    def log(self, msg):
        self.debug(msg)


    def debug_selected_elements(self):
        """Print debug information for each selected element."""
        selected_ids = self.svg.selected

# Example of checking inkex.__version__
        if hasattr(inkex, '__version__'):
            # selected_ids = self.svg.selected.id_dict();
            dump_object(selected_ids);
            for element in selected_ids:
                self.debug("El found" + element.tag)
            # print(f"Inkex version: {inkex.__version__}")
        else:
            self.log("inkex is old so shit is difrent ;(");

            # els = []
            # print("Inkex version not found, defaulting to 1.0")
            if not selected_ids:
                self.debug("No objects selected.")
                for element_id in selected_ids:
                    element = self.svg.getElement(element_id)
                    if element is not None:
                        self.debug("El found")
                        # els.push(element)
        return


                # print(f"Selected element ID: {element_id}, Tag: {element.tag}, Attributes: {element.attrib}")

    def effect(self):




        tmpsvg = self.svg_file



        filename = self.svg.name
        filepath = self.svg_path()

        extpath = self.ext_path()
        self.log("Tmp Svg: "+ tmpsvg)
        self.log("file Name: "+ filename)
        self.log("File Path: "+ filepath)

        self.log("inkex Path: "+ extpath)

        # webbrowser.get('firefox').open_new_tab(tmpsvg)
        file_path = tmpsvg
        if file_path and os.path.isfile(file_path):
            # Launch the live reload script in a detached subprocess
            subprocess.Popen(
                ['python3', extpath+'/geosvg_lib/live_reload.py', file_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                close_fds=True
            )
        else:
            inkex.utils.debug("Invalid file path")



        # livebrowser.live_reload(tmpsvg)

    # sp = self.svg_path()
    #     ep = self.ext_path()
        # ah = self.absolute_href()
        # dp = self.document_path()
        # id = get_inkscape_directory()


        # self.log(ep)
        # self.log(sp)
        #
        # self.log(id)

        # self.log(self.name())
        #
        # str = self.load_svg()
        #

        # dump_object(self.svg.metadata);


        # allEls = self.svg.ids
        self.log("selection ZONE")
        self.log("selection ZONE all Ids")
        # self.log(self.svg.ids.keys().join(", "));
        self.log(str(self.svg.get_ids()))

        self.log("selection ZONE")
        self.log("selection ZONE")

        self.debug_selected_elements()



        # dump_object(self.svg.metadata)
        self.log("SELF")
        dump_object(self);
        self.log("SELF.SVG")
        dump_object(self.svg);

        # dump_object(self.svg);



        self.log("SELF.document")
        # dump_object(self.document.getpath());
        dump_object(self.document.docinfo);

        self.log("SELF.original_document")
        # dump_object(self.original_document.getpath());
        dump_object(self.original_document.docinfo);
        self.log("INKEX.UTILS")

        dump_object(inkex.utils);
        self.log("INKEX")
        dump_object(inkex);


        # inx_file = os.path.join(os.path.dirname(__file__), 'geosvg_show_xml.inx')
        # if os.path.exists(inx_file):
        #     with open(inx_file, 'r', encoding='utf-8') as file:
        #         inx_content = file.read()
        #         self.debug("INX File Content:")
        #         self.debug(inx_content)
        # else:
        #     self.debug("Error: INX file not found.")

if __name__ == "__main__":
    e = GeoSVGShowXML()
    e.run()
