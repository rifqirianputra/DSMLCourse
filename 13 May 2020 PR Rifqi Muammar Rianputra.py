
# print("========SOAL 1=========")
# for baris in range(1,6):
#     for kolom in range(1, baris+1):
#         print(baris, end="    ")
#     print("\n")


# print("========SOAL 2=========")
# for baris in range(1,6):
#     for kolom in range(1, baris+1):
#         print(kolom, end="    ")
#     print("\n")

# print("========SOAL 3=========")
# for baris in range(5,-1,-1):
#     for kolom in range(5, baris,-1):
#         print(kolom, end="    ")
#     print("\n")

# print("========SOAL 4========")
# for baris in range(1,6):
#     for kolom in range(6, baris,-1):
#         print(baris, end="    ")
#     print("\n")


# print("========SOAL 5=========")
# for kolom in reversed(range(1,6)):
#     for baris in range(1, kolom+1):
#         print(baris, end="    ")
#     print("\n")

# print("========SOAL 6=========")
# for baris in range(5,0,-1):
#     for baris in reversed(range(1, baris+1)):
#         print(baris, end="    ")
#     print("\n")

# print("========SOAL 7=========")
# for i in range(6):
#     print('  ' * (5 - i)+' *  '*i) 

#LAT
# INPUT:MASUKKAN KALIMAT
# OUTPUT: KATA DALAM KALIMAT DIBALIK

# y = input(str("masukkan kalimat: "))
# x = list(y)

# for i in x:
#     i = x[::-1]
#     print(''.join(i))
#     break

# y = input(str("masukkan kalimat: "))
# x = y.split()
x = ['hari','kemarin','kamis'] #list(x)
x1 = ''
for i in x:
    x1 = i [::-1]
    i = (''.join(x1))
    print(i)