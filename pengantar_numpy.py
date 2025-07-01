"""
numpy adalah standart libry pyton yang digunakan untuk operasi numerik.
numpy menyediakan dalam bentuk array sangat mudah untuk memanipulasi ketimbang list
inti dari numpy adalah ndarray

beberapa properti dari ndarray
-ndim jumlah dimensi array
-shpe ukuran array setiap dimensi
-size total array dalam array
-dtype tipe data stiap elemen array
"""

import numpy as np

arr1 = np.array([12,12,1212,1,1])
print("array satu baris",arr1)
print("tipe data setiap elemen arrat", arr1.dtype)
print("ukuran array setiap elemen", arr1.shape)
print("ukuran array", arr1.size)


# Membuat array 2 dimensi
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray 2 dimensi:\n", arr2)

# Contoh array 3D (tensor)
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print(arr_3d)


# Operasi dasar pada array
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\nPenjumlahan array:", a + b)
print("Perkalian array:", a * b)
print("Rata-rata elemen:", np.mean(a))