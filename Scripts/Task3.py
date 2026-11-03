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

# List all feature classes within the Data folder that contains "BMR" in the name
BMR_list = arcpy.ListFeatureClasses("BMR*")
print(BMR_list)

# Iterate through each BMR file in the list, removing the last four characters (file suffix)
for file in BMR_list:
    BMR_file = file[:-4]
    print(BMR_file)
    arcpy.CreateFolder_management(scratch_path, f"{BMR_file}_folder")
    # Break the features of the BMR file by county features in teh TriCounties fc
        # use CO_NAME as the split field
        # direct outputs to the file made in this for loop
    arcpy.Split_analysis(file, "TriCounties.shp", "CO_NAME", scratch_path / f"{BMR_file}_folder")