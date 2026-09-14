import numpy as np
import time

# ==================================================
# 1. Create 1D, 2D and 3D arrays
# ==================================================

array_1d = np.array([10, 20, 30, 40, 50])

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("========== 1D ARRAY ==========")
print(array_1d)

print("\n========== 2D ARRAY ==========")
print(array_2d)

print("\n========== 3D ARRAY ==========")
print(array_3d)


# ==================================================
# 2. Array manipulation
# ==================================================

print("\n========== ARRAY SHAPE ==========")
print("1D shape:", array_1d.shape)
print("2D shape:", array_2d.shape)
print("3D shape:", array_3d.shape)

# Reshape
reshaped_array = np.arange(1, 10).reshape(3, 3)

print("\n========== RESHAPED ARRAY ==========")
print(reshaped_array)


# ==================================================
# 3. Vectorised operations
# ==================================================

numbers = np.array([10, 20, 30, 40, 50])

print("\n========== VECTORIZED OPERATIONS ==========")
print("Original:", numbers)
print("Add 10:", numbers + 10)
print("Multiply by 2:", numbers * 2)
print("Square:", numbers ** 2)

print("\n========== AGGREGATE OPERATIONS ==========")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))


# ==================================================
# 4. Aggregate across axes
# ==================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n========== AXIS OPERATIONS ==========")
print("Sum of all values:", np.sum(matrix))
print("Sum across rows:", np.sum(matrix, axis=1))
print("Sum across columns:", np.sum(matrix, axis=0))


# ==================================================
# 5. Boolean masking
# ==================================================

print("\n========== BOOLEAN MASKING ==========")

mask = numbers > 25

print("Mask:", mask)
print("Values greater than 25:", numbers[mask])


# ==================================================
# 6. Fancy indexing
# ==================================================

print("\n========== FANCY INDEXING ==========")

selected_values = numbers[[0, 2, 4]]

print("Selected values:", selected_values)


# ==================================================
# 7. Statistical measures
# ==================================================

data = np.array([10, 20, 30, 40, 50, 60, 70])

print("\n========== STATISTICAL MEASURES ==========")

print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("25th Percentile:", np.percentile(data, 25))
print("50th Percentile:", np.percentile(data, 50))
print("75th Percentile:", np.percentile(data, 75))


# ==================================================
# 8. Correlation
# ==================================================

sales = np.array([100, 200, 300, 400, 500])
advertising = np.array([20, 40, 60, 80, 100])

correlation = np.corrcoef(sales, advertising)[0, 1]

print("\n========== CORRELATION ==========")
print("Correlation between sales and advertising:", correlation)


# ==================================================
# 9. NumPy vs Python loop performance
# ==================================================

print("\n========== PERFORMANCE COMPARISON ==========")

size = 1_000_000

# Python list
python_numbers = list(range(size))

start_time = time.time()

python_result = [x * 2 for x in python_numbers]

python_time = time.time() - start_time


# NumPy array
numpy_numbers = np.arange(size)

start_time = time.time()

numpy_result = numpy_numbers * 2

numpy_time = time.time() - start_time


print("Python loop time:", python_time, "seconds")
print("NumPy time:", numpy_time, "seconds")

if numpy_time > 0:
    print("NumPy is approximately",
          round(python_time / numpy_time, 2),
          "times faster in this test.")


# ==================================================
# 10. Final message
# ==================================================

print("\n====================================")
print("NUMPY PRACTICE COMPLETED SUCCESSFULLY!")
print("====================================")