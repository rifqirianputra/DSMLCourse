#lambda
#lambda fungsinya untuk kode singkat
#lambda arguments


def myfunction(z):
    return lambda b: b * z

double = myfunction(2) # nilai z = 2
triple = myfunction(3) # nilai z = 3

print(double(11)) # 11 adalah nilai b
print(triple(11)) # 11 adalah nilai b

### map
## Function, mirip lambda
#iterable syntax
a = [2,3,4,5]
def kali(x):
    return x * 2
#cara 1
for i in a:
    print(kali(i))
#cara 2
b = list(map(kali,a))
print(b)
#cara 3
c = list(map(lambda x: x * 2, a))
print(c)



s = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda x: x%2==0, s))
print(result)

d = []
for i in s:
    if i%2==0:
        d.append(i)
print(d)




latihan 1
buat algoritma ----
buat list
pilihan : 
1 - ascending
2 - descending
#no functions,, reverse/::-1
output sesuai pilihan

latihan 2
buat algoritma
cari nilai maksmial dan minimal

latihan 3
buat algoritma
buat list
modus = 
median
median
q1/25%
q3/75%
outliers 

masuk ke algoritma


latihan 4
buat def atau functions
deret angka 
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
16,17,18,19,20
21,22,23,24,25

input= putar / spin /1-4
output
1 = 