import numpy as np

# Define the matrices
matrices_2x2 = [
    np.array([[-1, 2], [-2, -2]]),
    np.array([[1, 1], [2, 1]]),
    np.array([[-1, 1], [-2, -2]]),
    np.array([[-2, 2], [-2, -1]]),
    np.array([[2, 2], [-2, -2]]),
    np.array([[2, 2], [2, -2]]),
]

matrices_3x3 = [
    np.array([[-1, 0, 2], [-2, -2, 1], [1, 0, 2]]),
    np.array([[1, -1, 1], [0, -2, 0], [-2, -2, 2]]),
    np.array([[-2, -1, 0], [2, 2, 0], [-2, -2, 2]]),
    np.array([[2, 2, -2], [2, -1, 1], [0, 0, -1]]),
    np.array([[-2, -1, 2], [-1, 2, -2], [0, 2, -2]]),
]

matrices_4x4 = [
    np.array([[-1, 0, 2, 0], [-2, -2, 1, 1], [2, 0, 1, -1], [1, 0, -2, 0]]),
    np.array([[-2, -2, 2, -2], [0, -1, 0, 0], [2, 2, 0, -2], [-2, 2, 2, 2]]),
    np.array([[-2, 0, 0, 2], [-1, 1, 0, -1], [-2, -1, 2, -1], [0, 2, 0, -2]]),
    np.array([[2, 0, -2, 1], [-1, -2, 2, -2], [0, 0, 2, -1], [-2, 1, 0, -1]]),
    np.array([[0, -1, -2, 1], [2, 1, 0, 2], [1, 2, 1, 2], [0, 2, 1, 0]]),
    np.array([[0, -2, -1, -2], [2, 0, -2, -1], [-1, 2, -2, 1], [2, -1, 0, -2]]),
]

# Calculate determinants for 2x2 matrices
print("Determinants for 2x2 matrices:")
for i, matrix in enumerate(matrices_2x2):
    det = np.linalg.det(matrix)
    print(f"Matrix {i+1}: {det}")

# Calculate determinants for 3x3 matrices
print("\nDeterminants for 3x3 matrices:")
for i, matrix in enumerate(matrices_3x3):
    det = np.linalg.det(matrix)
    print(f"Matrix {i+1}: {det}")

# Calculate determinants for 4x4 matrices
print("\nDeterminants for 4x4 matrices:")
for i, matrix in enumerate(matrices_4x4):
    det = np.linalg.det(matrix)
    print(f"Matrix {i+1}: {det}")
