#%% Task 1e: Iterating through buffer distances
# Copy the script written from Task 1d.

import arcpy
import sys
from pathlib import Path

# Create path objects
script_path = Path(__file__).resolve().parent
print(script_path)
data_path = script_path.parent / "Data"
print(data_path)
scratch_path = script_path.parent / "Scratch"
print(scratch_path)

# Set arcpy workspace to the data filepath
arcpy.env.workspace = data_path
# Allow the script to overwrite any existing outputs
arcpy.env.overwriteOutput = True

# %% Run the buffer process using relative paths
streams_filepath = "streams.shp"
buff_dist = ["100", "200", "300", "400", "500"]

for dist in buff_dist:
    buff_filepath = scratch_path / f"buff_{dist}m.shp"
    print(buff_filepath)

    arcpy.Buffer_analysis(streams_filepath, buff_filepath, dist + ' meters', '', '', 'ALL')
    print(arcpy.GetMessages())

