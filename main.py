# Preparationg for Pair Coding Session

# STEP 1: Function to extract the needed data from netCDF file to a directory.
def extract_data(sentinel3_folder, output_folder):
    # Gather paths to NetCDF files and metdata xml file

    # Include timestamp in output_folder name

    # Extract from each NetCDF file the relevant bands

    pass

# STEP 2: Apply offset and fraction correction to data where needed.
def bias_correction():
    # TODO
    pass

# Step 3: Compute scaled Temperature T*.
def compute_scaled_temperature():
    # TODO
    pass

# Step 4: Filter pixels that are in the same area as clouds.
def filter_cloud_pixels():
    # TODO
    pass

# Step 5: Compute warm and cold edges.
def compute_edges():
    # TODO
    pass

# Step 6: Compute water stress and save to GeoTIFF file.
def compute_water_stress():
    # TODO
    pass