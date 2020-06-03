print("================================================")
print("==================SOAL NO 1=====================")
print("==========KALKULATOR NILAI UNTUK GURU===========")
print("================================================")
nilai_mtk = int(input("Please input MATH score: "))
    
if (nilai_mtk < 0 ) :
    print("please input a larger number and run the code again")
elif (nilai_mtk > 100):
    print("please input iua smaller number and run the code again")
else:
    print("thank you")

    nilai_bhs = int(input("Please input Bahasa Indonesia Score: "))

if (nilai_bhs < 0 ) :
    print("please input a larger number and run the code again")
elif (nilai_bhs > 100):
    print("please input a smaller number and run the code again")
else:
    print("thank you")

nilai_eng = int(input("Please input English score: "))
if (nilai_eng < 0 ) :
    print("please input a larger number and run the code again")
elif (nilai_eng > 100):
    print("mplease input a smaller number and run the code again")
else:
    print("thank you")

print("======================================================")

average_grade = ((nilai_bhs + nilai_eng + nilai_mtk)/3)
print("your average score is: " , round(average_grade))

if (nilai_mtk >= 90 and nilai_mtk <= 100):
    print("MATH PASSED, GRADE A")
elif (nilai_mtk >= 85 and nilai_mtk <= 89):
    print("MATH PASSED, GRADE A-")
elif (nilai_mtk >= 80 and nilai_mtk <= 84):
    print("MATH PASSED, GRADE B")
elif (nilai_mtk >= 75 and nilai_mtk <= 79):
    print("MATH PASSED, GRADE B-")
elif (nilai_mtk >= 70 and nilai_mtk <= 74):
    print("MATH PASSED, GRADE C")
elif (nilai_mtk >= 65 and nilai_mtk <= 69):
    print("MATH PASSED, GRADE D")
else:
    print("MATH FAILED, take a retest")

if (nilai_bhs >= 90 and nilai_bhs <= 100):
    print("BAHASA INDONESIA PASSED, GRADE A")
elif (nilai_bhs >= 85 and nilai_bhs <= 89):
    print("BAHASA INDONESIA PASSED, GRADE A-")
elif (nilai_bhs >= 80 and nilai_bhs <= 84):
    print("BAHASA INDONESIA PASSED, GRADE B")
elif (nilai_bhs >= 75 and nilai_bhs <= 79):
    print("BAHASA INDONESIA PASSED, GRADE B-")
elif (nilai_bhs >= 70 and nilai_bhs <= 74):
    print("BAHASA INDONESIA PASSED, GRADE C")
elif (nilai_bhs >= 65 and nilai_bhs <= 69):
    print("BAHASA INDONESIA PASSED, GRADE D")
else:
    print("BAHASA INDONESIA FAILED, take a retest")

if (nilai_eng >= 90 and nilai_eng <= 100):
    print("ENGLISH PASSED, GRADE A")
elif (nilai_eng >= 85 and nilai_eng <= 89):
    print("ENGLISH PASSED, GRADE A-")
elif (nilai_eng >= 80 and nilai_eng <= 84):
    print("ENGLISH PASSED, GRADE B")
elif (nilai_eng >= 75 and nilai_eng <= 79):
    print("ENGLISH PASSED, GRADE B-")
elif (nilai_eng >= 70 and nilai_eng <= 74):
    print("ENGLISH PASSED, GRADE C")
elif (nilai_eng >= 65 and nilai_eng <= 69):
    print("ENGLISH PASSED, GRADE D")
else:
    print("ENGLISH FAILED, take a retest")



if (nilai_bhs < 65):
    print("STUDENT FAILED A/SOME SUBJECT, PLEASE SEE CORRESPONDING TEACHER")
elif (nilai_eng < 65):
    print("STUDENT FAILED A/SOME SUBJECT, PLEASE SEE CORRESPONDING TEACHER")
elif (nilai_mtk < 65):
    print("STUDENT FAILED A/SOME SUBJECT, PLEASE SEE CORRESPONDING TEACHER")
else:
    print ("STUDENT PASS TO THE NEXT SEMESTER")

print("===========================================================")
print("================================================")
print("=================END OF SOAL 1==================")
print("================================================")
print("================================================")


print("================================================")
print("==================SOAL NO 2=====================")
print("======PROGRAM CEK PLAT NOMOR GENAP GANJIL=======")
print("================================================")


number = int(input("Please enter your license plate number ONLY, excluding letters: "))
if (number % 2) == 0:
    print("your plate is B", number , "XXX and allowed to drive through JL Jend Sudirman on EVEN calendar dates")
else:
    print("your plate is B", number , "XXX and allowed to drive through JL Jend Sudirman on ODD calendar dates")



print("================================================")
print("=================END OF SOAL 2==================")
print("================================================")
print("================================================")

print("================================================")
print("==================SOAL NO 3=====================")
print("=========PROGRAM CEK INDEX MASSA TUBUH==========")
print("================================================")

mass = int(input("Please enter your weight (in Kilograms): "))
print("your weight is ", mass, "Kg")
height = int(input("Please enter your height (in centimeters): "))
print("your height is ", height, "cm")

convert_cm = (height/100)
bmi = (mass/(convert_cm**2))

print("your body mass index number is:" , bmi)
print("you are categorized as")
if (bmi >= 40 ):
    print("Class 3 Obesity")
elif (bmi >= 35 and bmi < 40):
    print("Class 2 Obesity")
elif (bmi >= 30 and bmi < 35):
    print("Class 1 Obesity")
elif (bmi >= 25 and bmi < 30):
    print("Overweight")
elif (bmi >= 18.5 and bmi < 25):
    print("Normal Weight")
else:
    print("Underweight")


print("================================================")
print("=================END OF SOAL 3==================")
print("================================================")
print("================================================")



print("JCDS-PURWADHIKA BSD - RIFQI MUAMMAR RIANPUTRA")