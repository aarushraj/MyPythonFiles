import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Given data for consecutive months and incident counts
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
incident_counts = np.array([40, 22, 24, 21, 16, 19, 12, 12, 11, 8])

# Perform polynomial regression with a higher degree (degree 4)
degree_more_refined = 4
coeffs_more_refined = np.polyfit(months, incident_counts, degree_more_refined)

# Create the more refined polynomial equation
more_refined_polynomial_eq = Polynomial(coeffs_more_refined[::-1])

# Generate predicted values using the more refined equation
more_refined_incidents = more_refined_polynomial_eq(months)

# Print the final polynomial equation
equation_terms = [f"{coeff:.4f}x^{i}" if i > 0 else f"{coeff:.4f}" 
                  for i, coeff in enumerate(coeffs_more_refined[::-1])]
equation = " + ".join(equation_terms)

print("Final Polynomial Equation:")
print(f"y = {equation}")
