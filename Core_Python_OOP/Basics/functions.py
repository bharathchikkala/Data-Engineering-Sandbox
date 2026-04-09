#Function with inputs

def greet(name):
    print(f"Hey! {name}")
    print(f"How r u {name}")
    print(f"where r u {name}")
greet("ganga")
greet("bharath")
greet("sravani")


#Positional vs Keyword arguments

def function_name(name, location):
    print(f"My name is {name} and Iam from {location}")
function_name(name="ganga", location= "Amp")

#function with outputs

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("BhARATh","ganGA")

def ganga(f_name, l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return f"{formatted_f} {formatted_l}"
print(ganga("BhARATh","ganGA"))
