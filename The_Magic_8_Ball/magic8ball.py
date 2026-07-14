import random

question = input("Ask the Magic 8-ball a yes/no question: ")
answer_number = random.randint(1, 4)

if answer_number == 1:
    print("Magic 8-Ball says: Yes, definitely!")
elif answer_number == 2:
    print("Magic 8-Ball says: Reply hazy, try again later.")
elif answer_number == 3:
    print("Magic 8-Ball says: My sources say no.")
else:
    print("Magic 8-Ball says: Signs point to yes.")