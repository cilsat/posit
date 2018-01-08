#!/bin/bash

ogr2ogr -wrapdateline -t_srs EPSG:4326 $2 $1
