# def nama function ():
#     program

#driver code
#run
kurs = 14500

def intro(chambernum):
    print(f'welcome test chamber {chambernum}')
    print('please dial 0 on your phone')
    print('if you need anything')


intro('1102')

def namaitem():
    print('ini processor')

def hargaitem():
    namaitem()
    print('harga processor per item adalah USD 200')

def hargatotal(unit):
    hargaitem()
    harga = unit * 200 * kurs
    print(f'harga processor {unit} unit adalah {harga}')

hargatotal (6)




def BMI(berat=60,tinggi=1.85):
    result = berat/ (tinggi * 2)
    print('nilai bmi: ', result)

BMI (50,1.65) # urutan koma ngikut def BMI
BMI (berat = 45, tinggi = 1.55) #keyword (bisa dibalik)
BMI() #ngikut default number


def evenodd(num):
    if num%2 == 0:
        print('Even Number')
    else:
        print('Odd Number')

evenodd(19)