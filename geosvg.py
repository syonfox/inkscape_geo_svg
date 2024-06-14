# import inkex
#
# class GeoSVG(inkex.EffectExtension):
#     def add_arguments(self, pars):
#         pars.add_argument("--submenu", type=str, help="Submenu")
#         pars.add_argument("--title", type=str, help="Title")
#         pars.add_argument("--link", type=str, default="", help="Link")
#         pars.add_argument("--feature", type=str, default="", help="Feature")
#
#     def effect(self):
#         submenu = self.options.submenu
#         title = self.options.title
#
#         if submenu == "link_layer":
#             link = self.options.link
#             self.handle_link_layer(title, link)
#         elif submenu == "feature":
#             feature = self.options.feature
#             self.handle_feature(title, feature)
#         else:
#             inkex.utils.debug("Unknown submenu")
#
#     def handle_link_layer(self, title, link):
#         # Logic for handling Link Layer
#         inkex.utils.debug(f"Link Layer - Title: {title}, Link: {link}")
#
#     def handle_feature(self, title, feature):
#         # Logic for handling Feature
#         inkex.utils.debug(f"Feature - Title: {title}, Feature: {feature}")
#
# if __name__ == '__main__':
#     GeoSVG().run()
import json

#!/usr/bin/env python


import sys

import random
import math
from functools import cached_property

import inkex
from lxml import etree

prefix="geo"
nsuri = "http;//sgol.pub/geosvg"
inkex.NSS[prefix] = nsuri
# inkex.utils.NSS[prefix] = nsuri

# inkex.utils.SSN[nsuri] = prefix
etree.register_namespace(prefix, nsuri)

#
# def add_namespace(svg, prefix, url):
#     """Adds an xml namespace to the xml parser with the desired prefix.
#
#     If the prefix or url are already in use with different values, this
#     function will raise an error. Remove any attributes or elements using
#     this namespace before calling this function in order to rename it.
#
#     .. versionadded:: 1.3
#     """
#     if svg.nsmap.get(prefix, None) == url:
#         registerNS(prefix, url)
#         return
#
#     # Attempt to clean any existing namespaces
#     if prefix in svg.nsmap or url in svg.nsmap.values():
#         nskeep = [k for k, v in svg.nsmap.items() if k != prefix and v != url]
#         etree.cleanup_namespaces(svg, keep_ns_prefixes=nskeep)
#         if prefix in svg.nsmap:
#             raise KeyError("ns prefix already used with a different url")
#         if url in svg.nsmap.values():
#             raise ValueError("ns url already used with a different prefix")
#
#     # These are globals, but both will overwrite previous uses.
#     registerNS(prefix, url)
#     etree.register_namespace(prefix, url)
#
#     # Set and unset an attribute to add the namespace to this root element.
#     svg.set(f"{prefix}:temp", "1")
#     svg.set(f"{prefix}:temp", None)

# inkex.elements._utils.registerNS("geo2", "http;//sgol.pub/geosvg2")
def dump_object(obj):
    for attribute in dir(obj):
        try:
            value = getattr(obj, attribute)
            inkex.utils.debug(f"{attribute}: {value}")
        except AttributeError:
            inkex.utils.debug(f"{attribute}: Attribute not accessible")

dump_object(inkex)

dump_object(inkex.utils)

class GeoSVG(inkex.EffectExtension):
    # def add_arguments(self, pars):
    #     pars.add_argument("--submenu", type=str, help="Submenu")
    #     pars.add_argument("--title", type=str, help="Title")
    #     pars.add_argument("--link", type=str, help="Link")
    #     pars.add_argument("--feature", type=str, help="Feature")
    #
    # def effect(self):
    #     submenu = self.options.submenu
    #     title = self.options.title
    #     link = self.options.link
    #     feature = self.options.feature
    #
    #     inkex.utils.debug(f"Submenu: {submenu}")
    #     inkex.utils.debug(f"Title: {title}")
    #     inkex.utils.debug(f"Link: {link}")

    #     inkex.utils.debug(f"Feature: {feature}")
    def __init__(self):
        inkex.Effect.__init__(self)

        self.arg_parser.add_argument("--namespace",
                                     type=str,
                                     default="https://sgol.pub/geosvg",
                                     help="Namespace URI to add to the root tag")
        self.arg_parser.add_argument("--prefix",
                                     type=str,
                                     default="geo",
                                     help="Namespace prefix to add to the root tag")


        self.arg_parser.add_argument("-n", "--name",
                                     type=str,
                                     dest="name", default="geosvg1",
                                     help="Css Class to add to main svg")
        self.arg_parser.add_argument("-t", "--title",
                                     type=str,
                                     dest="title", default="Click Me",
                                     help="A tooltip/title tag contents")
        self.arg_parser.add_argument("-d", "--desc",
                                     type=str,
                                     dest="desc", default='{type:"Feature"}',
                                     help="The GeoJSON Feature to embed in this tag")
        # self.arg_parser.add_argument("-c", "--class",
        #                              type=str,
        #                              dest="class", default="class1",
        #                              help="CSS classes to add")
        self.arg_parser.add_argument("-cs", "--clear_styles",
                                     type=inkex.Boolean,
                                     dest="clear_styles", default=False,
                                     help="Clear inline styling")
        self.arg_parser.add_argument("-p", "--preview",
                                     type=inkex.Boolean, default=False,
                                     help="Show Preview")


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

    def setNS(self):
        # Get the root element of the SVG document
        root = self.document.getroot()

        # extra_nss_str = json.dumps(self.base.extra_nss)
        # inkex.utils.errormsg(extra_nss_str)
        # Get the namespace URI and prefix from the arguments
        namespace_uri = self.options.namespace
        namespace_prefix = self.options.prefix
    # Add the new namespace to the nsmap

        if prefix not in root.nsmap:
            root.nsmap[prefix] = nsuri;
            # Debug output to check the nsmap
            self.debug(f"Updated nsmap: {root.nsmap}")

        self.svg.set("geo:version", "1")
        # note root and self.svg are the same


        # Add the namespace to the root tag using addNS
        # new_tag = inkex.utils.addNS(root.tag, namespace_prefix)

        # Add the namespace declaration to the root element
        # root.set(f'xmlns:{namespace_prefix}', namespace_uri)

        # ret = inkex.utils.addNS(root.tag, "xmlns:geo='http://sgol.pub/geosvg")

        # (self.svg
        #  .add_namespace(namespace_prefix, namespace_uri))

        # self.extra_nss = {"geo": "http://sgol.pub/geosvg"}
        # self.svg.set("xmlns:geo", "http;//sgol.pub/geosvg")
        # inkex.utils.addNS("geo", "http;//sgol.pub/geosvg2")
        # self.svg.nsmap["geo"] = "http;//sgol.pub/geosvg"
        # self.svg.set("geo:version", "1")
        # self.svg.set("geo2:version", "2")

        dump_object(self.svg)

        # Debug output
        # self.log(f"Updated self.extra_nss, {self.extra_nss}")
        self.log(f"Added namespace {namespace_prefix} with URI {namespace_uri}")



    def effect(self):

        newclass = self.options.name
        elements = self.svg.selected.values()

        self.setNS()


        for el in elements:
            current_classes = el.attrib.has_key("class") and el.attrib["class"].split() or []


            if newclass not in current_classes:
                current_classes.append(newclass)
                self.debug("Adding Class To: "+ el.attrib["id"])

            if self.options.clear_styles:
                el.attrib.pop("style", None)

            el.attrib["class"] = " ".join(current_classes)
        # self.attr_update(attr)
        # self.debug("Done Geo SVG")


        self.clean_up()




if __name__ == '__main__':
    e = GeoSVG()
    e.run()
