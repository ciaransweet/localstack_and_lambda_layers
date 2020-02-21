import numpy
import pygeos
import rasterio
import requests
import rio_cogeo
import rio_color
import rio_tiler
import rio_tiler_mosaic
import rio_tiler_mvt
import shapely
import supermercado


def handler(event, context):
    print(numpy.__version__)
    print(pygeos.__version__)
    print(rasterio.__version__)
    print(requests.__version__)
    print(rio_cogeo.version)
    print(rio_color.__version__)
    print(rio_tiler.version)
    print(rio_tiler_mosaic.version)
    print(rio_tiler_mvt.__version__)
    print(shapely.__version__)
    print(supermercado.__package__)
    return {"message": "Printed all versions"}
