def add(*args):
    for n in args:
        print(n)

add(1,20,15,4)

def adds(n1= 12,n2=12):
    return n1+n2
print(adds())



def calculator(**kwargs):
    for key, value in kwargs.items():
        print(key)
        #print(value)

calculator(add=5,multiply=20)
