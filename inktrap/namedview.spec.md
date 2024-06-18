# Ink Trap

### Draw Constrained

---

### Introduction

Ink Trap is a highly efficient software designed to facilitate seamless and unconstrained 
editing of SVG images and files. Inspired by the motto "Draw Freely" from the Ink Scape project, 
Ink Trap aims to provide a streamlined user experience. However, to enhance usability and 
efficiency, it is necessary to impose certain constraints on the software.

**"Where there is complexity there is inefficiency." — Kier's Law**

To increase efficiency and offer value within our GeoSVG suite, we must necessarily constrain 
the scope of SVG and geospatial features.

### Constraints

1. **Data Size**
    - **5-10MB:** This constraint allows for fluid rendering of images on the web, ensuring that performance is not compromised.

2. **Input Format**
    - **GeoJSON:** Utilizing GeoJSON as the input format is essential. While it may be inefficient and verbose, its universality and human readability make it the standard choice.
      ```json
      {
        "type": "FeatureCollection",
        "features": [...]
      }
      ```

3. **Output Format**
    - **SVG Rendering by Leaflet:** The output should be in SVG format, as rendered by Leaflet, with one group containing many paths.
      ```xml
      <svg>
        <g class="geo-svg-layer"> # this is optional but a nice to have
          <path class="geo-svg-feature" d="..." />
          ...
        </g>
      </svg>
      ```
      
4. 

## Olv version 

https://gitlab.com/inkscape/inkscape/-/blob/master/src/extension/implementation/script.cpp#L532

