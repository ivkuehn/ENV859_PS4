#%% Task 3 

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

BMR_list = arcpy.ListFeatureClasses("BMR*")
print(BMR_list)

for file in BMR_list:
    arcpy.CreateFolder_management(scratch_path, f"{file}_folder")