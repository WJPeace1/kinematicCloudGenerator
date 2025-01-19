
import numpy as np

# # Dimensions # #
# Tank
T = 0.2 # tank diameter
R = T/2 # tank radius
H = T # tank height
D = T/3 # impeller diameter
R_shaft = 0.004 # impeller shaft radius
B = 0.725*R # baffle length

# Rotating zone
# 
r_zone = (0.75 / 3) * T
y_min_zone = (0.75 / 3) * T
y_max_zone = (1.25 / 3) * T

# Number of particles
n_particles = 5400
d_particles = 300e-06
# Point generation

positions = []

while len(positions) < n_particles:

    theta = np.random.uniform(0,2*np.pi)
    y = np.random.uniform(0,(H-5*d_particles))

    if y < y_min_zone:    
        r = np.sqrt(np.random.uniform((0+(3*d_particles))**2,(B-(3*d_particles))**2))
    
    elif y > y_max_zone:
        r = np.sqrt(np.random.uniform(R_shaft**2,(B-(3*d_particles))**2))
    
    elif y_min_zone < y < y_max_zone:
        r = np.sqrt(np.random.uniform((r_zone+(3*d_particles))**2,(B-(5*d_particles))**2))

    x = r * np.cos(theta)
    z = r * np.sin(theta)

    positions.append((x,y,z))

with open("particle_positions", "w") as f:
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

print("writing complete")