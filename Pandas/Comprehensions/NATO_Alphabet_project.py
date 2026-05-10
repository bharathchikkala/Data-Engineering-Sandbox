import pandas
# with open("nato_phonetic_alphabet.csv") as csvfile:
#     file = csvfile.read()
#     print(file)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
new_dict = {row.letter : row.code for (index,row) in data.iterrows()}
# print(new_dict)
game_is_on = True
while game_is_on:
    name = input("Enter your name: ").upper()
    # new_list = []
    # for letter in name:
    #     go_to_list = new_dict[letter]
    #     new_list.append(go_to_list)
    # print(new_list)

    #using list comprehension

    new_list = [new_dict[letter] for letter in name]
    print(new_list)
    again = input("Do you want to run again 'yes' or 'no' : ").upper()
    if again == "Y":
        game_is_on = True
    else:
        game_is_on = False
