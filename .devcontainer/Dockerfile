FROM osgeo/gdal:ubuntu-full-3.4.0

RUN apt-get update && apt-get install -y python3-pip git
RUN pip3 install --upgrade pip
RUN pip3 install numpy fiona rioxarray xarray rasterio datetime netCDF4 pandas geopandas
