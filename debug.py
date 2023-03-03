from osgeo import gdal

def try_ReadAsArray(path):
    
    print(f"Try ReadAsArray on {path}")
    ds = gdal.Open(path)
    array = ds.ReadAsArray()
    print(array.shape)

if __name__ == "__main__":
    try_ReadAsArray("data/DEBUG_example/labels.tif")