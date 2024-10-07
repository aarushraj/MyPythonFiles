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

# Plot the data
plt.figure(figsize=(10, 6))

# Plot the equations
plt.plot(months, y_values_eq1, label="Observation 1 (Eq: 0.299x^2 - 6.013x + 40.05)", color='orange', linewidth=2)
plt.plot(months, y_values_eq2, label="Observation 2 (Eq: -0.102x^3 + 1.988x^2 - 13.803x + 48.833)", color='darkblue', linewidth=2)

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
