
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

print("========SOAL 7=========")
y=('')
z=('')
for baris in range(1,9):
    for kolom in range(1, baris+1):
        z += ("   ")
    z += ("\n")
    for baris in range(5,9):
        for kolom in range(1, baris+1):
            y += (" * ")
            y += ("\n")
print(z)