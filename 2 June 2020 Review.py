# buah = ['mangga', 'jeruk', 'apel', 'alpukat']
# kombinasi = ['susu','keju','coklat','apel','mangga']

#list comprehension
#gak boleh ada yang sama

# z = [1,2,3,4]
# kombo = [[i**2,i**3]for i in z]
# print(kombo)

# gabung = []
# for i in buah:
#     for j in kombinasi:
#         if i == j:
#             gabung.append(j)
# print(gabung)

# gabung = [(i,j) for i in buah for j in kombinasi if i !=j]
# print(gabung)



# angka = 1
# while angka < 10:
#     print(angka)
    
#     angka += 1
# print('====================')
# for i in range (1,10):
# #     print(i)
# print('====================')
# for i in range (1,9):
#     if i == 5:
#         break
#     print(i)
# print('====================')
# for i in range (1,9):
#     print(i)
#     if i == 5:
#         break



# print('====================')
# for i in range (1,10):
#     if i == 5:
#         continue
#     print(i)
# print('====================')
# for i in range (1,9):
#     print(i)
#     if i == 5:
#         continue



##### data structure
#list = []

nilai = [8,9,10,22,13,23,11]
for i in nilai:
    print(i)

print(nilai[:])

#slicing nilai [start:end:step] index angka pertama adala 0

print (nilai[0])
print (nilai[:3])
print (nilai[::-1])
nilai.sort()
print(nilai)

nilai.append(90)
print(nilai[:])


### Tuple === (),tuple(), (data)
a = 200
b = 300
c = 600

d = 1,2,3,4,5,6

print(d)