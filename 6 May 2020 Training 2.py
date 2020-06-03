import math

total_hari = int(input("masukkan jumlah hari: "))
tahun = math.floor(total_hari/360)
leftoveryear = total_hari % 360
bulan = math.floor(leftoveryear / 30)
leftovermonth = leftoveryear % 30
minggu = math.floor(leftovermonth / 7)

print ("jumlah hari yang anda masukkan adalah:", total_hari , "yang terdiri dari, " , tahun, "tahun" , bulan , "bulan" , minggu , "minggu")

print("================================================")

print("WELCOME TO RECTANGLE VOLUME CALCULATOR")
length = int(input("please enter your object length "))
width = int(input("please enter your object width "))
height = int(input("please enter your object height "))

print("your rectangle volume is:")
print(length * width * height)


print("===============================================")
print("WELCOME TO CIRCLE SURFACE AREA CALCULATOR")
radius = int(input("please enter your circle radius "))
area = ((math.pi) * radius**2)
circumference = (2* math.pi *radius)
print("your circle radius is", radius, "so that means your circle area is" , round(area,7), "and the circumeference of the circle is" , round(circumference,7))

print("===============================================")

string = input("masukan kalimat: ")
convertlow = string.lower()
letterinput = input("masukan huruf: ")
letterinputlower = letterinput.lower()
count = convertlow.count(letterinputlower)
print(f"Jumlah huruf {letterinput} pada kalimat {string} adalah {count}")


