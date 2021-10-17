import numpy as np

print("********************************")
#1)100 adet 5 barındıran bir array oluşturun.

print(np.ones(100)*5)
print("********************************")
#2) 1'den 100'e kadar 3' bölünebilen sayıları yazdırın.

print(np.arange(2,100,2))
print("********************************")
#3) 2 adet matris oluşturup çarpın.
A = [[2, 3, 1], [2, 4, 1]]
B = [[3, 1, 4], [2, 1, 3], [1, 2, 2]]

arr = np.array(A)
arr2 = np.array(B)

sonuc = np.dot(arr, arr2)
print(sonuc)
print("********************************")
#4) 3.işlemin sonucunun transpozunu alın.

transpoze = sonuc.T
print(transpoze)
print("********************************")

#5) 4.işlem sonunda oluşan matrisin içindeki değerlerin ortalamasını bulun.

print(transpoze.mean())