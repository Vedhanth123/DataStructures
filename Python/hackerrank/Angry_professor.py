# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

import random

def angryProfessor(k, a):
    
    no_of_students_early = 0

    for x in range(len(a)):

        if(a[x] <= 0):
            no_of_students_early += 1
        
    if(no_of_students_early >= k):
        return "NO"
    else:
        return "YES"


test_cases = []

for length_of_array in range(20):

    test_cases.append(random.randint(-100,100))

print(test_cases)

k = random.randint(0,len(test_cases))

print(k)



print(angryProfessor(3, [-1, -3, 4, 2]))