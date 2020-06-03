import math
print("====================== JAWABAN SOAL 1======================")
years_past = 19
years_difference_past = 0.5
difference_ratio_past = 1/4
years_difference_now = 19
difference_ratio_now = 1/7
mom_age_now = 49
mom_age_past = (mom_age_now - years_past)

daughter_age_now = (years_difference_now + mom_age_now/7)
daughter_age_past = (daughter_age_now - years_past)

print("the mother gave birth to her daughter at", (mom_age_past - daughter_age_past) , "years old")

print("======================END OF SOAL 1======================")

print("====================== JAWABAN SOAL 2======================")


total_age_now = 50
years_past = 4
number_of_people = 2
total_age_past = (total_age_now - (number_of_people * years_past))
past_andi_age = (1) #assumtion number, because dad's age is 6 times more, that means son's age is 1x
past_dad_age = (1 * 6) #assumption number, dad's age is 6 times more than the son
combined_difference = (past_andi_age) + (past_dad_age)
division = total_age_past / combined_difference
andi_age_now = (division * past_andi_age + years_past)
dad_age_now = (division * past_dad_age + years_past)

print("Jawaban 2")
print(f"andi age is {andi_age_now} years old, while his dad is {dad_age_now} years old")

print("  ==================END OF SOAL 2======================")