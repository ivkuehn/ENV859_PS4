#%% Task 2

## Path Variables Setup
import arcpy
from pathlib import Path

script_path = Path(__file__).resolve().parent
print(script_path)
data_path = script_path.parent / "Data"
print(data_path)
scratch_path = script_path.parent / "Scratch"
print(scratch_path)

arcpy.env.overwriteOutput = True

#%% ArcPy Wrangling

roads = data_path / "Roads.shp"
road_type = "0;201;203"
road_type_list = road_type.split(';')
for type in road_type_list:
    road_type_attr = f'"ROAD_TYPE" = {type}'
    roads_out = scratch_path / f"roads_out_{type}.shp"
    arcpy.Select_analysis(roads, roads_out, road_type_attr)
    arcpy.GetMessages()
