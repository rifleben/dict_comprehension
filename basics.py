# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
space = "----------------------------- \n"

# basic dict comprehension with random int as value and list for keys:
names = ["John", "Sara", "Bethany", "Kyle", "Deirdre", "Benny"]
students_scores = {student: random.randint(1, 100) for student in names}
print(f"Our entry list was {names}")
print(f"Our dictionary result is, {students_scores}")
print(space)

# ---------------------#


# basic dict comprehension with conditionals

passed_students = {student:score for (student, score) in students_scores.items() if score > 70}
print(f"Our entry dict was {students_scores}")
print(f"Our dictionary result is, {passed_students}")

print(space)