import arcpy
from arcpy import sa
import os

# Allow overwriting, after importing modules.
arcpy.env.overwriteOutput = True

# Get parameters from the tool
input_fn = arcpy.GetParameterAsText(0)   # Input raster, must be .tif
output_dir = arcpy.GetParameterAsText(1) # Output folder, must be a folder

# Check if output_dir exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Creates a hillshade from the elvation data
hillshade_out = os.path.join(output_dir, "hillshade.tif")
hilsh = sa.Hillshade(input_fn, 315, 45, 'SHADOWS', 0.00001)
hilsh.save(hillshade_out)

# Creates contours from the elvation data.
# These are set at 100 meter intervals by default.
# You can change that number but it may take much longer to run.
contour_out = os.path.join(output_dir, "contours.shp")
contours = sa.Contour(input_fn, contour_out, 100)

# Creates slope raster from elevation data.
slope_out = os.path.join(output_dir, "slope.tif")
slope = sa.Slope(input_fn)
slope.save(slope_out)

# Creates aspect data from elevation data.
aspect_out = os.path.join(output_dir, "aspect.tif")
aspect = sa.Aspect(input_fn)
aspect.save(aspect_out)

#Confirmation message
arcpy.AddMessage("All outputs saved to: " + output_dir)
