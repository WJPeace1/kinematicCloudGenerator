# # # Kinematic Cloud Positions Generator # # #

import os
import numpy as np

# # Dimensions # #
# Tank
T = 0.2
R = T/2
H = T-0.005
D = T/3
B = 0.7 * R

# Rotating Zone
T_zone = 0.09
R_zone = T_zone/2
y_min = 0.05
y_max = 0.0767

# Number of particles
n = 3600

# # Generation of points # #
# y-axis is vertical
# x-axis and z-axis are side-to-side
positions = []

while len(positions) < n:
    theta = np.random.uniform(0, 2*np.pi)
    r = np.sqrt(np.random.uniform(R_zone**2,B**2))

    y = np.random.uniform(0,H)
    x = r * np.cos(theta)
    z = r * np.sin(theta)

    positions.append((x,y,z))

# # Writing positions to OpenFOAM format # #
    
with open("kinematicCloudPositionsNEW_2", "w") as f:
    f.write("FoamFile\n{\n")
    f.write("    version     2.0;\n")
    f.write("    format      ascii;\n")
    f.write("    class       vectorField;\n")
    f.write("    object      kinematicCloudPositions;\n")
    f.write("}\n")
    f.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n")
    f.write("(\n")
    for pos in positions:
        f.write(f"    ({pos[0]} {pos[1]} {pos[2]})\n")
    f.write(")\n")
    f.write("// ************************************************************************* //\n")