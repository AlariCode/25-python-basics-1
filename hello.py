grades = [95, 48, 76, 59, 88]
# [95, "не сдал", 76, "не сдал", 88]

for i, grade in enumerate(grades):
    if grade < 60:
        grades[i] = "не сдал"
print(grades)
