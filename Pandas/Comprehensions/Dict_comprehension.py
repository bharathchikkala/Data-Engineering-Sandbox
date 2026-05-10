#dict comprehensions
import random

dict_names = ["akka", "raja", "bharath"]
scores = {them : random.randint(20, 100) for them in dict_names}
print(scores)


passed_students = {student:score for (student,score) in scores.items() if score >= 50}
print(passed_students)
