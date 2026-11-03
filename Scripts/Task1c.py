#%% Task 1c: Enabling user input
# Copy the script written from Task 1b.

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
buff_filepath = sys.argv[2]
print(buff_filepath)

arcpy.Buffer_analysis(streams_filepath, buff_filepath, buff_dist + ' meters', '', '', 'ALL')
print(arcpy.GetMessages())