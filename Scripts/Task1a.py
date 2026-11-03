#%% Task 1a: Creating the initial buffer script
# This task will buffer the Streams.shp file by 1000 meters, generating a new output file StrmBuff1km.shp

import arcpy

streams_filepath = "V:/ENV859_PS4/Data/streams.shp"
buff_dist = "1000 meters"
buff_filepath = "V:/ENV859_PS4/Scratch/strmbuff1km.shp"

arcpy.Buffer_analysis(streams_filepath, buff_filepath, buff_dist, '', '', 'ALL')
print(arcpy.GetMessages())

