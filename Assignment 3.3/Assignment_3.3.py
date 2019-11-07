score = input("Enter Score: ")
s=float(score)
if 0.9 <= s <= 1.0:
    grade = "A"
elif 0.8 <= s < 0.9:
    grade = "B"
elif 0.7 <= s < 0.8:
    grade = "C"
elif 0.6 <= s < 0.7:
    grade = "D"
elif s < 0.6:
    grade = "F"

print(grade)