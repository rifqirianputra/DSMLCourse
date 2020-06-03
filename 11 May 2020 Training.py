## list, tubple

## set -> not in order -> no indexing -> unique

data = {5,8,'test',9} #<-- bisa menerima apapun kecuali list
print(data)
angka = (2,4,3,6,4,6,5,4,3,4,6,7,9,8,7,8,6,8,7,6,5,6,4,3,2,1,3,4,5,2,4,3,6,4,6,5,4,3,4,6,7,9,8,7,8
,6,8,7,6,5,6,4,3,2,1,3,4,5)
data1 = set(angka)

print(data1)
print(8 in data1)
data1.update([100,99,23,24,54,32,51,'shit']) # update <<<< multiple data
print(data1)

data1.add('crap') # <<<< only 1 argument (1 data only)
print(data1)

data1.remove('shit')
print(data1)
data1.discard('crap') #no error
print(data1)

# ========= UNION ==========
data1.clear()
print(data1)

x = {1,2,3,4,5}
y = {1,2,4,8,9}

print(x.union(y))
print(y.union(x))
print (x | y)
print (y | x)

# ========= INTERSECTION ============

print(x.intersection(y))
print(y.intersection(x))

print (x & y)
print (y & x)

# ========== DIFFERENCE ============ NON REVERSIBLE
print(x.difference(y))
print(y.difference(x))

print(x-y)
print(y-x)

# ========== SYMMETRICAL DIFFERENCE ============

print(x.symmetric_difference(y))
print(y.symmetric_difference(x))

print(x^y)
print(y^x)