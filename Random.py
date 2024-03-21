import random

my_answers= [
"no",
"yes",
"I dont wanna",
"bye bye",
"Definently", 
"not at all",
"Yeppers", 
"ew no you sicko",
"Skibidi correct", 
"sigma wrong",
]

while  True:
    my_number = random.randrange(0, 9)
    question = input("what would you like to ask the magick eight ball?")
    print(my_answers[my_number])
    ask_again = input("Would you like to ask again?")
    if ask_again != "yes":
        print("thanks for asking so long gay bowser")
        break

# print(my_number)
# Ninja whaaa?