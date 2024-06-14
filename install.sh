#!/bin/bash

INKSCAPE_EXTENSION_DIR="$HOME/.config/inkscape/extensions/"


cp -r  geosvg_lib $INKSCAPE_EXTENSION_DIR


cp geosvg.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg.py $INKSCAPE_EXTENSION_DIR

cp geosvg_debug_log.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg_debug_log.py $INKSCAPE_EXTENSION_DIR

cp geosvg_debug_show_versions.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg_debug_show_versions.py $INKSCAPE_EXTENSION_DIR

cp geosvg_debug_show_xml.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg_debug_show_xml.py $INKSCAPE_EXTENSION_DIR

cp geosvg_pop_python.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg_pop_python.py $INKSCAPE_EXTENSION_DIR


cp geosvg_debug_pipe_cat.inx  $INKSCAPE_EXTENSION_DIR
cp geosvg_debug_pipe_cat.sh $INKSCAPE_EXTENSION_DIR
