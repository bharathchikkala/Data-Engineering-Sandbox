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
