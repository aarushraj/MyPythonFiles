import numpy as np
import matplotlib.pyplot as plt

# Define months and the actual incident counts
months = np.arange(1, 11)  # Months from 1 to 10
actual_counts = [40, 22, 24, 21, 16, 19, 12, 12, 11, 8]

# Define the equations
def equation1(x):
    return 0.299 * x**2 - 6.013 * x + 40.05

def equation2(x):
    return -0.102 * x**3 + 1.988 * x**2 - 13.803 * x + 48.833

# Generate y-values based on the equations
y_values_eq1 = equation1(months)
y_values_eq2 = equation2(months)

# Define the new equation
def equation3(x):
    return 61.5833 - 30.1494 * x + 7.9696 * x**2 - 0.9197 * x**3 + 0.0372 * x**4

# Generate y-values based on the new equation
y_values_eq3 = equation3(months)

# Plot the data with the new equation
plt.figure(figsize=(10, 6))

# Plot the previous equations
plt.plot(months, y_values_eq1, label="Observation 1 (Eq: 0.299x^2 - 6.013x + 40.05)", color='orange', linewidth=2)
plt.plot(months, y_values_eq2, label="Observation 2 (Eq: -0.102x^3 + 1.988x^2 - 13.803x + 48.833)", color='darkblue', linewidth=2)

# Plot the new equation
plt.plot(months, y_values_eq3, label="Observation 3 (Eq: 61.5833 - 30.1494x + 7.9696x^2 - 0.9197x^3 + 0.0372x^4)", 
         color='green', linewidth=2)

# Plot the actual readings
plt.scatter(months, actual_counts, label="Actual Incident Count", color='red', marker='x', s=100)

# Customize the plot
plt.xlabel('Month')
plt.ylabel('Incident Count')
plt.title('Comparison of Observations with Actual Incident Count')
plt.xticks(months)  # Set the x-axis to show months
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
