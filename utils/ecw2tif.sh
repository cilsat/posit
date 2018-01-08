#!/bin/bash

# Convert ECW to GTiff optimized for map serving
echo "Converting to GTiff"
gdal_translate -of GTiff -co bigtiff=yes -co compress=jpeg -co jpeg_quality=50 \
  --config GDAL_TIFF_INTERNAL_MASK YES -co tiled=yes -co photometric=ycbcr \
  --config GDAL_CACHEMAX 4096 -b 1 -b 2 -b 3 "$1" "$2"

# Add overviews to allow for easier browsing
echo "Adding overviews"
gdaladdo --config compress_overview jpeg --config jpeg_quality 50 \
  --config photometric_overview ycbcr --config interleave_overview pixel \
  --config GDAL_CACHEMAX 4096 -r average "$2" 2 4 8 16 32 64
