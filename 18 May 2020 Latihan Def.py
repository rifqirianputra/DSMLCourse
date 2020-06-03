
#LAT 1 DONE!!!

#kalkulator +,-,/,*
#def input angka
#def input angka
#input operator
#output hasil kalkulasi
loopcontrol = ''
# def calcadd(num1,num2):
#     result = num1 + num2
#     print(result)
# def calcsub(num1,num2):
#     result = num1 - num2
#     print(result)
# def calcmult(num1,num2):
#     result = num1 * num2
#     print(result)
# def calcdiv(num1,num2):
#     result = num1/num2
#     print(result)

# while loopcontrol !=1:
#     print("===========================================================================")
#     print('[1] Addition. [2] Subtraction. [3] Multiplication. [4] Division. [5] Exit  ' )
#     print("===========================================================================")
#     calcselect = int(input('please select your calculator '))
#     if calcselect == 1:
#         num1 = int(input('please enter your first number:  '))
#         num2 = int(input('please enter your second number:  '))        
#         print("=============ANSWER=============")
#         print(f'{num1} added by {num2} is:')
#         calcadd(num1,num2)
#         print("================================")
#     elif calcselect == 2:
#         num1 = int(input('please enter your first number:  '))
#         num2 = int(input('please enter your second number:  '))
#         print("=============ANSWER=============")
#         print(f'{num1} subtracted by {num2} is:')
#         calcsub(num1,num2)
#         print("================================")
#     elif calcselect == 3:
#         num1 = int(input('please enter your first number:  '))
#         num2 = int(input('please enter your second number:  '))
#         print("=============ANSWER=============")
#         print(f'{num1} multiplied by {num2} is:')
#         calcmult(num1,num2)
#         print("================================")
#     elif calcselect == 4:
#         num1 = int(input('please enter your first number:  '))
#         num2 = int(input('please enter your second number:  '))
#         print("=============ANSWER=============")
#         print(f'{num1} divided by {num2} is:')
#         calcdiv(num1,num2)
#         print("================================")
#     elif calcselect == 5:
#         print('Program Terminated')
#         break
#     else:
#         print('please select the correct number')
# LAT 2 WORDS - > MORSE BERHASIL.. MORSE - > WORDS GAGAL
# dict dan def
# morse code decryptor
# loopcontrol = ''
# morse_dictionary =  {'A':'.-', 'B':'-...', 
#                     'C':'-.-.', 'D':'-..', 'E':'.', 
#                     'F':'..-.', 'G':'--.', 'H':'....', 
#                     'I':'..', 'J':'.---', 'K':'-.-', 
#                     'L':'.-..', 'M':'--', 'N':'-.', 
#                     'O':'---', 'P':'.--.', 'Q':'--.-', 
#                     'R':'.-.', 'S':'...', 'T':'-', 
#                     'U':'..-', 'V':'...-', 'W':'.--', 
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..', 
#                     '1':'.----', '2':'..---', '3':'...--', 
#                     '4':'....-', '5':'.....', '6':'-....', 
#                     '7':'--...', '8':'---..', '9':'----.', 
#                     '0':'-----', ' ':' '} 

# def alphatomorse():
#     listcovert = list(userinput)
#     for key in listcovert:
#         convert = (morse_dictionary.get(key))
#         print(convert,end='')
# def morsetoalpha():
#     listcovert = list(userinput)
#     reversed_morse_dictionary = {value : key for (key, value) in morse_dictionary.items()}
#     for key in listcovert:
#         convert = (reversed_morse_dictionary.get(key))
#         print(convert,end='')

# print("===========================================================================")
# print("=========================  MORSE CODE TRANSLATOR  =========================")
# print("NOTE: for alphabet to morse code, please only enter words and letters")
# print("NOTE: for morse to alphabet, please only use '.' dots and '-' dashes")
# print("===========================================================================")
# while loopcontrol != 1:
#     userinput = input("please input items to decrypt/encrypt:   ").upper()
    
#     if all(i.isalpha() or i.isspace() for i in userinput):
#         alphatomorse()
#         break
#     else:
#         morsetoalpha()
#         break

# LAT 3 DONE!!!
# Fizz= habis dibagi 3
# Buzz= habis dibagi 5
# Fizz Buzz = habis dibagi 3 dan 5
# def fizzbuzz(num):
#     if num%3 == 0 and num%5 == 0:
#         print('Fizz Buzz')
#     elif num%3 == 0:
#         print('Fizz')
#     elif num%5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# num = int(input('enter a number '))
# for i in range(1,num):
#     fizzbuzz(i)




# LAT 4 DONE, tapi terpaksa liat internet
# Caesar Cipher
# input kata
# input angka maju
# result
import string
allchar = string.printable
listchar = list(allchar)
while loopcontrol != 1:

    def caesar(words,numbersofjump):
        encrypted = ''
        for i in range(len(words)):
            j = words[i]
            if (j.isupper()): 
                encrypted += chr((ord(j) + numbersofjump-65) % 26 + 65)
            else: 
                encrypted += chr((ord(j) + numbersofjump - 97) % 26 + 97)
        return (encrypted)

    words = input('please enter the word to cipher: ')
    numbersofjump = int(input('please enter a number to jump: '))
    print('encrypted: '+ caesar(words,numbersofjump))
    



# LAT 5 ->>> ARABIC TO ROMAN BERHASIL, ROMAN TO ARABIC NGGAK
# ROMAN - ARABIC NUMBERAL CONVERTER 
# MAX 4000
# arb_num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
# rom_num = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
# def arabicconverter(num):
#     value = 0
#     roman = ""
#     convertinput = ''
#     while num > 0:
#         for i in range(num // arb_num[value]):
#             roman += rom_num[value]
#             num -= arb_num[value]
#         value += 1
#     return roman
#     print(arabicconverter())

# def romanconverter():
#     convertlist = list(userinput)
#     for i in convertlist:
#         if userinput == rom_num['']:
#             print('1000')

# while loopcontrol !=1:
#     print("======================================================================")
#     print("================= ARABIC / ROMAN NUMERALS CONVERTER ==================")
#     print("======================================================================")
#     userinput = input('please enter your number: ')
#     checkinput = userinput.isnumeric()
#     if checkinput == True:
#         print('Arabic to Roman')
#         convertinput = int(userinput)
#         print(arabicconverter(convertinput))
#     elif checkinput == False :
#         print('Roman to Arabic')
#         print(romanconverter())
#         break


#LAT 6 - >
#enter digital number
#eg = 6
#output = 
# __
#|__
#|__|