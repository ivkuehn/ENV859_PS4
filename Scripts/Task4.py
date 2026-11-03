#%% Task 4

# Goal is to create a describe object for a user-specified dataset
    #  then send messages to the ArcGIS model based on the dataset properties

# Tip: create code to initially print the messages instead of sending them

import arcpy

input_dataset = arcpy.GetParameterAsText(0)

# Need to get the catalogPath for the input dataset
dataset_path = arcpy.da.Describe(input_dataset)
#print(f"Catalog Path: {dataset_path['catalogPath']}")
arcpy.AddMessage(f"Catalog Path: {dataset_path['catalogPath']}")

# Report the XMin, YMin, XMax, and YMax properties of the dataset's extent object
data_xmin = dataset_path['extent'].XMin
data_ymin = dataset_path['extent'].YMin
data_xmax = dataset_path['extent'].XMax
data_ymax = dataset_path['extent'].YMax
#print(f"XMin: {data_xmin}")
arcpy.AddMessage(f"XMin: {data_xmin:.1f}")
#print(f"YMin: {data_ymin}")
arcpy.AddMessage(f"YMin: {data_ymin:.1f}")
#print(f"XMax: {data_xmax}")
arcpy.AddMessage(f"XMax: {data_xmax:.1f}")
#print(f"YMax: {data_ymax}")
arcpy.AddMessage(f"YMax: {data_ymax:.1f}")

# Check the datasetType
type = dataset_path['datasetType']

if type == "FeatureClass":
    shape_type = dataset_path['shapeType']
    #print(f"Shape Type: {shape_type}")
    arcpy.AddWarning(f"Shape Type: {shape_type}")
elif type == "RasterDataset":
    data_format = dataset_path['format']
    data_rows = dataset_path['height']
    data_cols = dataset_path['width']
    #print(f"Format: {data_format}")
    #print(f"# of rows: {data_rows}")
    #print(f"# of columns: {data_cols}")
    arcpy.AddWarning(f"Format: {data_format}")
    arcpy.AddWarning(f"# of rows: {data_rows}")
    arcpy.AddWarning(f"# of columns: {data_cols}")
else:
    #print(f"Data Type: {type}")
    arcpy.AddError(f"Data Type: {type}")