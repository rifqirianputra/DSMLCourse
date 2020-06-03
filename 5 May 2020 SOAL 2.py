
print("=======SOAL 2========")


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