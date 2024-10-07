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

# Calculate the differences between the actual counts and the values from the equations
diff_eq1 = np.abs(actual_counts - y_values_eq1)
diff_eq2 = np.abs(actual_counts - y_values_eq2)
# Define the new equation
def equation3(x):
    return 61.5833 - 30.1494 * x + 7.9696 * x**2 - 0.9197 * x**3 + 0.0372 * x**4

# Generate y-values based on the new equation
y_values_eq3 = equation3(months)

# Calculate the differences between the actual counts and the values from all equations
diff_eq3 = np.abs(actual_counts - y_values_eq3)

# Create a comparison table for all three equations
comparison_table_all = {
    'Month': months,
    'Actual Count': actual_counts,
    'Observation 1 (Eq 1)': y_values_eq1,
    'Error (Eq 1)': diff_eq1,
    'Observation 2 (Eq 2)': y_values_eq2,
    'Error (Eq 2)': diff_eq2,
    'Observation 3 (Eq 3)': y_values_eq3,
    'Error (Eq 3)': diff_eq3
}
import pandas as pd
# Convert the dictionary to a pandas DataFrame for a nice display
comparison_df_all = pd.DataFrame(comparison_table_all)

from IPython.display import display
display(comparison_df_all)


