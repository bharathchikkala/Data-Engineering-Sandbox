try:
    file = open("file20.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file2 = open("file20.txt", "w")
    file2.write("ok written")

except KeyError as a:
    print(f"key {a} not found")

else:
    content = file.read()
    print(content)

finally:
    # raise TypeError ("rasina code mottam selav") zip(data["student"], data["marks"])
    file.close()
    print("file is closed")

dict = {
    "student" : ["bharath", "ganga"],
    "marks" : [90, 120]
}
print(dict["marks"][0])
for student, mark in zip(dict["student"], dict["marks"]):
    if mark > 100:
        raise ValueError("marks should be less than 100")
print(dict["student"][0])
