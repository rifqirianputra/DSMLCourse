
# # SOAL 1 
# # list data structured
# # input: masukkan nama hari
# # jumlah: -2 hari
# # output:
# # 100 hari dari sekarang adalah hari

# days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


# userinputdays = str(input("what day is today? ")).lower()

# if (userinputdays == "monday"):
#     convert = 0
# elif (userinputdays == "tuesday"):
#     convert = 1
# elif (userinputdays == "wednesday"):
#     convert = 2
# elif (userinputdays == "thursday"):
#     convert = 3
# elif (userinputdays == "friday"):
#     convert = 4
# elif (userinputdays == "saturday"):
#     convert = 5
# elif (userinputdays == "sunday"):
#     convert = 6
# else:
#     print("please enter the correct day")
    
# userinputduration = int(input("how many days to fast forward? "))
# for i in days:
#     print(days[(convert+userinputduration%7)])


# #==========================

# # SOAL 2
# # palindrome
# # input: masukkan kalimat
# # kondisi dilakukan pengecekan kalimat
# # output: kata itu palindrome/tidak

# palindromeornot = str(input("masukkan kata yang ingin kamu cek: ")).lower()
# convertlist = list(palindromeornot)
# reversal = convertlist [::-1]

# if (convertlist == reversal):
#     print("it's a Palindrome! congrats")
# else:
#     print("not a Palindrome, try again!")

# #==========================
# # SOAL 3
# # masukkan kalimat: hari ini hari selasa
# # ada 2 opsi
# # opsi 1 = masukkan karakter a
# # opsi 2 = ubah huruf vokal
# # output: hri ini hri sels


inputuser = str(input("masukkan kalimat: "))

opsiuser = str(input("masukan 'opsi 1' untuk menghilangkan huruf, masukan 'opsi 2' untuk merubah huruf, dan 'opsi 3' untuk mengubah seluruh vokal: "))
if (opsiuser == "opsi 1"):
    inputuserremove = str(input("masukkan huruf yang ingin dihilangkan: "))
    print("dari kalimat", inputuser, ", anda ingin menghilangkan huruf", inputuserremove,".")
    print("maka kalimat anda menjadi....")
    answer = list(inputuser)
    for letter in answer:
        if letter == inputuserremove:
            answer.remove(letter)
            print(''.join(answer))

elif (opsiuser == "opsi 2"):
    whattoreplace = str(input("masukkan huruf yang ingin anda ubah: "))
    inputuserreplace = str(input("masukkan huruf pengganti: "))
    print("dari kalimat", inputuser, ", anda ingin mengganti huruf",whattoreplace, "dengan" ,inputuserreplace,".")
    print("maka kalimat anda menjadi....")
    answer = list(inputuser)
    for letter in answer:
        if letter == whattoreplace:
            answer = [item.replace(whattoreplace, inputuserreplace) for item in answer]
            print(''.join(answer))
elif (opsiuser == "opsi 3"):
        print("anda ingin mengganti seluruh huruf vokal" )
        vokalreplacement = str(input("masukkan huruf pengganti "))
        print("dari kalimat", inputuser, ", anda ingin mengganti seluruh huruf vokal dengan," ,vokalreplacement,)
        print("maka kalimat anda menjadi....")
        replacedvokal = str(inputuser.replace("a", vokalreplacement))
        replacedvokal2 = str(replacedvokal.replace("i", vokalreplacement))
        replacedvokal3 = str(replacedvokal2.replace("u", vokalreplacement))
        replacedvokal4 = str(replacedvokal3.replace("e", vokalreplacement))
        replacedvokal5 = str(replacedvokal4.replace("o", vokalreplacement))
        print(replacedvokal5) 
else:
    print("masukkan opsi yang benar")


# # # ==========================
# # SOAL 4
# # hanya menggunakan metode numerikal
# # masukkan 4 digit angka: 5689
# # outputnya 8956
# # jika input string = "angka yang anda masukkan salah"

# angka = input("masukkan empat digit angka ")
# limitintonly = angka.isdigit()
# if (limitintonly == True):
#     angka = list(map(int, str(angka)))
#     list1 = angka[0:2]
#     list2 = angka[2:4]
#     flip = (list2+list1)
#     for i in flip:
#         print(i, end="")
# else:
#     print("hanya masukkan angka")



# # ==========================
# # SOAL 5
# # masukkan angka 2 digit: 85
# # masukkan angka 2 digit 32
# # output = 8532
# jika input string = "angka yang anda masukkan salah"

# num1 = input("masukkan 2 digit angka ")
# num2 = input("masukkan 2 digit angka ")
# limitintonly1 = num1.isdigit()
# limitintonly2 = num2.isdigit()
# if (limitintonly1 and limitintonly2 == True):
#     listnum1 = list(num1)
#     listnum2 = list(num2)
#     listnum1.extend(listnum2)
#     for i in listnum1:
#         print(i, end="")
# else:
#     print("hanya masukkan angka")
