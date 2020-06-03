x = list(range(1,21))
a = []
b = []
c = []
d = []
e = []

for i in range(1,21):
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)


for angka1 in range(2,21):
    for angka2 in range(2,angka1):
        if angka1 % angka2 == 0:
            e.append(angka1)
            break
    else:
        d.append(angka1)

for i in range(-20,0):
    c.append(i)

dataf = [a,b]
# for y in dataf:
#     break

f = dataf

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


password = "rahasia"
cek = ''
passenter = 1
maxenter = 5

while cek != password:
    if passenter <= maxenter:
        cek = input('enter password: ')
        if cek != password and passenter < 5:
            passenter += 1
            print('percobaan ke ', passenter, ", salah. coba lagi")
        elif cek != password and passenter ==5:
            passenter += 1
            print("try again later")
            break
        else:
            print("loggin in")