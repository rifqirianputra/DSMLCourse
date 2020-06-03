# ### LAMBDA, MAP, DAN FILTER

# #Lambda = anonymous function, one time use, small size
# #basic syntax:

# a = lambda agrument: print(agrument)
# a('selamat pagi')
# print(a)

# kuadrat= lambda x: x**2
# print(kuadrat(5))

# def kuadrat2(x):
#     return x ** 2

# print(kuadrat2(5))

# pangkat = lambda x, y: x ** y

# print(pangkat(5,2))

# cek = lambda x: True if x%2 == 0 else False
# print(cek(29))
# print(cek(20))

# cek = lambda x: 'genap' if x%2 == 0 else 'ganjil'
# print(cek(29))
# print(cek(20))


# a = [1,2,3,4,5]
# b = []
# print(kuadrat(2))

# for i in a:
#     b.append(kuadrat2(i))
# print(b)
# c = list(map(kuadrat2,a))
# print(c)

# def pangkat2(x,y):
#     return x**y

# d= list(map(pangkat2,a,c))
# print(d)

# e = list(map(pangkat2, a, list(list(map(kuadrat2,a)))))
# print(e)  

### FILTER ========

#fliter(function, iterabledata) hanya ambil true berdasarkan function
from functools import reduce

# b = list(range(1,201))
# odd = list(filter(lambda x: x%2 != 0, list(range(1,201))))
# pangkat = list(map(lambda x: x ** 3, (list(filter(lambda x: x%2 != 0, list(range(1,201)))))))
hasil = reduce(lambda x,y: x+y, list(map(lambda x: x ** 3, (list(filter(lambda x: x%2 != 0, list(range(1,201))))))))
print(hasil)