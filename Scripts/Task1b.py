#%% Task 1b: Using relative paths and environment values in your script

# Import necessary packages
import arcpy
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
buff_dist = "1000 meters"
buff_filepath = scratch_path / "strmbuff1km.shp"

arcpy.Buffer_analysis(streams_filepath, buff_filepath, buff_dist, '', '', 'ALL')
print(arcpy.GetMessages())
