import numpy as np
import geopandas as gpd
import psycopg2 as pg
import rasterio
import rasterio.mask


def mask_raster(raster, shapes, save_path=None):
    if type(shapes) != list:
        shapes = [shapes]

    out_img, out_tform = rasterio.mask.mask(raster, shapes, crop=True)
    if not save_path:
        return out_img
    else:
        out_meta = raster.meta.copy()
        out_meta.update({'driver': 'GTiff',
                         'height': out_img.shape[1],
                         'width': out_img.shape[2],
                         'transform': out_tform})
        with rasterio.open(save_path, 'w', **out_meta) as dst:
            dst.write(out_img)


def get_data_by_block(block, tables=['block', 'sawit', 'landuse']):
    con = pg.connect(database='ehp', user='postgis',
                     password='postgis', host='/run/postgresql')
    data = {t: gpd.read_postgis("select * from " + t + " where blok_1 = '" + block "'"), con) for t in tables}
    return data
