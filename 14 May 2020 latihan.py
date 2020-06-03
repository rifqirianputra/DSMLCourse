# input : translate (idn to eng) atau (eng to idn)
# pilih nama hari
# kalau kosong = nama hari salah

# print(nama hari {hari1} dalam bahasa inggris adalah {hari1{enterhari}})

hari = {
    
    "senin":"monday",
    "selasa":"tuesday",
    "rabu":"wednesday",
    "kamis":"thursday",
    "jumat":"friday",
    "saturday":"sabtu",
    "sunday":"minggu"
}

# translate = {
#     [1. IDN - ENG] [2. ENG - IDN]
# }

# listhari = list(hari)
# days = list(hari.values())
# print(listhari)
# print(days)


# while(True):
#     for i in translate:
#         print(i)
#     opsiuser = int(input('masukkan pilihan anda / please input your selection: '))
#     if opsiuser == 1:
#         indo = str(input('masukkan nama hari: ').lower())

        
# menu = ""
# opsiuser = int(input("pilih opsi translasion/select your translation option.. 1 untuk IDN -> ENG || 2 for ENG -> IDN "))
# if opsiuser == 1:
#     enterhari = input('masukkan nama hari: ').lower()
#     print(f'nama hari {enterhari} dalam bahasa Inggris adalah: {hari1[enterhari]}')
# elif opsiuser == 2:
#     for i in hari.items():
#         print(i)
#         print(type(i))
# else:
#     print('masukkan angka yang benar / please enter the correct number')

indo = list(hari.keys())
eng = list(hari.values())
print(indo)
print(eng)