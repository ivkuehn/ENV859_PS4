#%% Task 5

# Import necessary packages
import arcpy
import sys

# Create two user inputs: a feature class and field from that feature class
feature = sys.argv[1]
field = sys.argv[2]

# Create a point object
point = arcpy.Point(X=597000, Y=249000)

# Create a SearchCursor
rows = arcpy.da.SearchCursor(feature,[f'{field}', 'SHAPE@'])
# Use a For loop to iterate through all rows
for row in rows:
    feature_field = row[0]
    recShape = row[1] 
    # If TRUE, determine attribute value of the user input field
    if recShape.contains(point):
        print(f"The point is contained in {feature_field} county.")
        # Send message back to ArcGIS Pro indicating what the field's value is for the record
        arcpy.AddMessage(f"County: {feature_field}")
