#%% Task 1d: Adding auto-generated output names.
# Copy the script written from Task 1c.

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
buff_dist = sys.argv[1]
print(buff_dist)
buff_filepath = scratch_path / f"buff_{buff_dist}m.shp"
print(buff_filepath)

arcpy.Buffer_analysis(streams_filepath, buff_filepath, buff_dist + ' meters', '', '', 'ALL')
print(arcpy.GetMessages())