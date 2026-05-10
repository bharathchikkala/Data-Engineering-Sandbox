#list comprehensions
#new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [num +1 for num in numbers]
# new_list.append(numbers)
print(new_list)

name = 'bharath'
new_li = [letter for letter in name]
print(new_li)

number_range = range(1,5)
new__list = [n*2 for n in number_range]
print(new__list)

#conditional list comprehension
names = ["ganga", "akka", "raja"]
list_new = [name.upper() for name in names if len(name) == 4]
print(list_new)
