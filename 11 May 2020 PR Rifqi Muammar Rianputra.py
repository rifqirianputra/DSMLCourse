# A = himpunan bilangan genap dari 1 - 20
# B = himpunan bilangan ganjil dari 1 - 20
# C = himpunan bilangan negatif lebih dari -20
# D = himpunan bilangan prima dari 1 - 20
# E = himpunan bilangan komposit 1 -20
import math

x = set(range(1,21))
a = set(range(2,21,2))
b = set(range(1,21,2))
c = set(range(-20,0))
# d = {2,3,5,7,11,13,17,19} << TARGET BILANGAN PRIMER
# e = {4,6,8,9,10,12,14,15,16,18,20} << TARGET BILANGAN KOMPOSIT
d1 = []
e1 = []

for angka1 in range(2,21):
    primetest = True
    for angka2 in range(2,angka1):
        if angka1 % angka2 == 0:
            primetest = False
            e1.append(angka1)
            break
    if primetest:
        d1.append(angka1)
d = set(d1)
e = set(e1)
            

print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
print("==========SOAL A=========")
print(a|b|c|d|e)
print("=========SOAL B==========")
print((a & b) | (d & e))
print("==========SOAL C=========")
print((a | b) & (d | e))
print("=========SOAL D==========")
print((a | b) - (d | e))
print("=========SOAL E==========")
print((a | b | c) - (a & e))