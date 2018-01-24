#!/usr/bin/env python

import os
import geopandas as gpd
import rasterio
import rasterio.mask
from shapely.geometry import mapping
import psycopg2 as pg

from utils import mask_raster

ortho_path = '/home/cilsat/data/map/EHP/ECW ORTOFOTO/1701_EHP-ADS_Ortho_9,3 cm_buffer 50_rev1.3.tif'
shp_path = '/home/cilsat/data/map/EHP/SHP SAWIT ADS/ads_sawit.shp'
train_path = '/home/cilsat/dev/posit/sawit/train'
con = pg.connect(database='ehp', user='postgis',
                 password='postgis', host='/run/postgresql')


def gen_train_data(block='A01'):
    # Use queries to postgis to save some memory
    sawit = gpd.read_postgis(
        "select geom from sawit where blok = '" + block + "'", con)
    # buffer size is determined visually here: it depends on raster scale
    bboxes = sawit.geometry.apply(lambda x: x.buffer(0.000045, cap_style=3))
    feats = [mapping(b) for b in bboxes]

    with rasterio.open(ortho_path) as src:
        for i, f in enumerate(feats):
            dst_path = os.path.join(
                train_path, block + str(i).zfill(5) + '.tif')
            mask_raster(src, f, dst_path)


def main():
    # Train an ensemble of discriminative classifiers, with each classifier
    # trained against a different class as the negative
    pass


if __name__ == '__main__':
    gen_train_data()
