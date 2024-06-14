# Ink Trap 

Draw Constrained.

SVG 1 group and paths

each path has an desc

each desc is a GeoJSON feature


## System

### Local Computer
```txt
[Inkscape] <-> [inktrap.py / inktrap_server.py] 
               [ localhost:7449 get (inktrap) ]
                    |
                    V
            [POST /api/free/inktrap]
            [CloudFlare Pages Function]->[KV storeage]
                                             \       
                                             [kv get]
                    [FreeMap Display Rotated Overlay ]



V2 

[Inkscape]   <---------------------------------------------------.
     \                                               :            \
[FileSystem /tmp/ink_ext_IN_XXX and /tmp/ink_ext_OUT_XXX ] ---> [inkex plugin]
                  |                                  ^------------+
                  v                                               |
[Browser / GeoSvg Editor]-----------------------------------------'

```


### Requirements

ONLY tested on linux (debian stable) todo test on windows ;) 

```sh
apt install inkscape ; # 1.0.2+
apt install firefox ; 
apt install featherpad ;
```

### Install 

```sh 
apt install git ; 

git clone https://github.com/syonfox/inkscape_geo_svg.git

cd inkscape_geo_svg

bash install.sh
```

### Developers 

```sh
git clone git@github.com:syonfox/inkscape_geo_svg.git
cd inkscape_geo_svg
bash install.sh
echo "todo write tests"
```
Get Svg from inkscape. Export to Raster if over 24mb b64

# File extentions

`inx` - an inkscape xml spec for plugin defonition/ ui
`py` - a pyhtong script to handel the plugin aruments
`html` - an html web page for th ebrowser
`js` - a javascript for the browser

