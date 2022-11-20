# take input of all the absenties
absenties = input("").split(",")
absenties = list(map(lambda x: int(x), absenties))

dict_of_students = {}

for x in range(1, 88):
    if (x < 66 or x > 80):
        dict_of_students[x] = 0

print("--------------------------------------- Printing Absenties ------------------------------------")
print(absenties)

print("-------------------------------------------- Students in class ---------------------------------------")
for x in dict_of_students.keys():
    print(f"Roll No. {x}: {dict_of_students[x]}")


print("--------------------------------------------- Assigning attendance ----------------------------------")
for x in dict_of_students.keys():
    if (x not in absenties):
        dict_of_students[x] += 1

for x in dict_of_students.keys():
    print(f"Roll No. {x}: {dict_of_students[x]}")

