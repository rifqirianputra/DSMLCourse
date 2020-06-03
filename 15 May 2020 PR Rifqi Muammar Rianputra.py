#input: masukkan alamat email

#kondisi: memilik format (nama@namahosting.ekstensi)
#         nama user hanya boleh, huruf, angka, dan underscore, dan titik
#         nama hosting hanya boleh huruf dan angka
#         ekstensi hanya boleh huruf dan maksimal 5 karakter

#output: alamat email yang anda masukkan tidak valid
#output: alamat email yang anda masukkan valid
# import re

# regularex = '[\w-]+(\.[\w-]+)*@([a-z0-9-]+(\.[a-z0-9-]+)*?\.[a-z]{2,6}|(\d{1,3}\.){3}\d{1,3})(:\d{4})?$'
# looptest = ''

# print("============ EMAIL VALIDATION ============")
# print("========== WITH REG EX FUNCTION ==========")
# print('\n')
# print('\n')
# while looptest != 1:
#     emailinput = input("please enter your email address: ").lower()
#     if re.match(regularex,emailinput):
#         print('thank you for entering your email address')
#         break
#     else:
#         print('invalid email address')

# print('\n')
# print('\n')
# print('\n')

import string
print("============= EMAIL  VALIDATION =============")
print("=========  WITH NO REG EX FUNCTION  =========")
print('\n')
print('\n')
loopcontrol = ''
acceptedstr = list(string.ascii_lowercase)
acceptednum = [0,1,2,3,4,5,6,7,8,9]
acceptedsym = ['_','@','.',]
char = acceptednum+acceptedstr+acceptedsym
acceptedchar = list(map(str,char))
allchar = string.printable.lower()
setallchar = set(allchar)
setacceptchar = set(acceptedchar)
setunaccept = setallchar - setacceptchar
unacceptchar = list(setunaccept)
        
while loopcontrol != 1:
    emailinput = input("please enter your email address: ").lower()
    listemail = list(emailinput)
    for i in listemail:
        if any(let in listemail for let in unacceptchar):
            print(f'"{emailinput}"" is an INVALID email address \n try again')
            break
        else:
            firstsplit = emailinput.split('@')[1]
            secondsplit = emailinput.split('@')[-1]
            endsplit = secondsplit.split('.')
            if len(endsplit) == 2:
                splitend1 = secondsplit.split('.')[-1]
                if len(splitend1) <= 5:
                    print(f'"{emailinput}"" is a VALID email format')
                    break
                
                else:
                    print(f'"{emailinput}"" is an INVALID email address \n try again')
            elif len(endsplit) == 3:
                splitend1 = secondsplit.split('.')[-1]
                splitend2 = secondsplit.split('.')[-2]
                if len(splitend1) <= 5 and len(splitend2) <= 5:
                    print(f'"{emailinput}"" is a VALID email format')
                    break
                else:
                    print(f'"{emailinput}"" is an INVALID email address \n try again')
                    break


print("=============================================")
print("=============================================")
print("===========Rifqi Muammar Rianputra===========")
print("=============Purwadhika BSD JCDS=============")

