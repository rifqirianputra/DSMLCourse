# #FOR IF IN

# #for namavariabel in () #string gak bisa masuk, () harus multiple isinya

# fruits = ["Watermelon", "Apple", "Banana", "Tomato", "Kiwi"]
# for i in fruits:   
#     print(i)

# print('=======================')

# print(range(0,10,1))

# print('=======================')

# for i in range(10):
#     print(i)

# print('=======================')
# for i in range(1,11):
#     if i%2 == 0:
#         print('genap')
#     else:
#         print(i)

# for i in range(1,100):
#     if i == 78:
#         print('data found')
#         break
#     print(i)


# fruits = ['watermelon', 'apple', 'banana', 'tomato', 'kiwi']
# vegetable = ['carrot', 'cucumber','kale','spinach','tomato']
# data = [fruits,vegetable]
# for i in data:
#     print(i)
#     for j in i:
#         print(j)

# z = ('')
# for item in range(1):
#     for item1 in range (0,item+1):
#         z += '*'
#     z += '\n'

# print(z)

x = list(range(1,21))
a = []
b = []

for angka1 in range(1,21):
    if angka1 %2 == 0:
        a.append

c = list(range(-20,0))
d = []
e = []
for angka1 in range(2,21):
    primetest = True
    for angka2 in range(2,angka1):
        if angka1 % angka2 == 0:
            primetest = False
            e.append(angka1)
            break
    if primetest:
        d.append(angka1)

dataf = [a,b]
for y in dataf:
    print(dataf)
    break


print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
