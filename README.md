# Install

Geoplot requires quite a few things. Easiest thing to do is use `conda`. Otherwise...

## proj4

```
wget http://download.osgeo.org/proj/proj-4.9.3.tar.gz
```

## tkinter

```
apt-get install python3-tk
```

## shapely

Make sure to install the "no binary" version (and have geos-3.4+ installed). Otherwise, you'll run into a runtime assertion failure :(

```
pip uninstall shapely &&
pip install shapely --no-binary :all:
```


# More Sources of Raw Data
*  https://www.mass.gov/service-details/massgis-data-layers 
