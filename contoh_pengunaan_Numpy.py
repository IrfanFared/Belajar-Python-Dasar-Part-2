import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Penjumlahan
sum_arr = arr1 + arr2
print("Penjumlahan:", sum_arr)

# Pengurangan
sub_arr = arr2 - arr1
print("Pengurangan:", sub_arr)

# Perkalian (element-wise)
mul_arr = arr1 * arr2
print("Perkalian (element-wise):", mul_arr)

# Pembagian
div_arr = arr2 / arr1
print("Pembagian:", div_arr)

# Perkalian skalar
scalar_mul = arr1 * 3
print("Perkalian Skalar:", scalar_mul)

print("-" * 30)

# Operasi pada array 2D
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Penjumlahan matriks
sum_matrix = matrix1 + matrix2
print("Penjumlahan Matriks:\n", sum_matrix)

# Perkalian matriks (dot product)
dot_product = np.dot(matrix1, matrix2)
# Atau bisa juga: dot_product = matrix1 @ matrix2 (untuk Python 3.5+)
print("Perkalian Matriks (Dot Product):\n", dot_product)