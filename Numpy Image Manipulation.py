
import numpy as np
# import io module from scikit image which enables us to read in an image 
from skimage import io
import matplotlib.pyplot as plt

camaro = io.imread("camaro.jpg")
# We can see it is just an array filled with numbers
print(camaro)

# Use shape atttribute to look at the structure of our image
# The output of this is telling us that the image has 1200 rows of pixels, 1600 columns of pixels and is a 3D array
# 3D array because it is a colour image
camaro.shape

# To view the image 
plt.imshow(camaro)
plt.show()

# Cropping the image 

# This first attempt showed that the first axis is the y axis. The colon means that we want everything from the other two axis
cropped = camaro[0:500, :, :]
plt.imshow(cropped)
plt.show()

# This time lets try and crop along the x axis
cropped = camaro[:, 400:1000, :]
plt.imshow(cropped)
plt.show()

# Now that we have this information we can attempt to crop just the car
cropped = camaro[350:1100, 200:1400, :]
plt.imshow(cropped)
plt.show()

# Save this new cropped image into our folder 
io.imsave("camaro_cropped.jpg", cropped)

# Flip our image using array slicing (uses start:stop:step logic, hence the double colon then -1 to flip)

vertical_flip = camaro[::-1, :, :]
plt.imshow(vertical_flip)
plt.show()
io.imsave("camaro_vertical_flip.jpg", vertical_flip)

horizontal_flip = camaro[:, ::-1, :]
plt.imshow(horizontal_flip)
plt.show()
io.imsave("camaro_horizontal_flip.jpg", horizontal_flip)

# Colour channels

# Create a zeros array that is the same size and dimention as the image
red = np.zeros(camaro.shape, dtype = "uint8")

# Fill in the rows and columns with the values for only the red channel and leave the other two channels as zeros
red[:,:,0] = camaro[:,:,0]
plt.imshow(red)
plt.show()
# The same applies for green and blue, just need to change the index of the colour channel that we are referring to
green = np.zeros(camaro.shape, dtype = "uint8")
green[:,:,1] = camaro[:,:,1]
plt.imshow(green)
plt.show()

blue = np.zeros(camaro.shape, dtype = "uint8")
blue[:,:,2] = camaro[:,:,2]
plt.imshow(blue)
plt.show()

# Use stack function to stack these three colour images on top of each other
camaro_rainbow = np.vstack((red,green,blue))
plt.imshow(camaro_rainbow)
plt.show()
plt.imsave("camaro_rainbow.jpg", camaro_rainbow)


































