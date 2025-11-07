
"""
Much quicker to use numpy than loops for calculations with high volumes of data. The calcualtion
for this task takes a fraction of a second
"""

import numpy as np

# Create a 1D array containing the radius for the all the planets 
radii = np.array([2439.7, 6051.8, 6371, 3389.7, 69911, 58232, 25362, 24622])

# calculate the volume of each planet using the radii values and formula below
volumes = 4/3 * np.pi * radii**3
print(volumes)

# Below code will show how to calculate the volumes for 1,000,000 planets 
# This demonstrates the efficiency of numpy by rapidly performing calculations for such large volumes of date
radii = np.random.randint(1, 1000, 1000000)
volumes = 4/3 * np.pi * radii**3
print(volumes)
