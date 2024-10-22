import numpy as np
import matplotlib.pyplot as plt

# Define the Mandelbrot function
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Set up the plot dimensions and parameters
width, height = 800, 800
max_iter = 100

# Create a 2D array to store the results
mandelbrot_set = np.zeros((width, height))

# Define the complex plane dimensions
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

# Generate the Mandelbrot set
for x in range(width):
    for y in range(height):
        real = x_min + (x / width) * (x_max - x_min)
        imag = y_min + (y / height) * (y_max - y_min)
        c = complex(real, imag)
        mandelbrot_set[x, y] = mandelbrot(c, max_iter)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_set.T, cmap='twilight', extent=[x_min, x_max, y_min, y_max])
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
