import random


answer = random.randint(1, 9)
user_input = ""
count = 0
while user_input != answer and user_input != "exit":
    user_input = input("guess the number ")
    if user_input == "exit":
        break


    count += 1

    if int(user_input) > answer:
        print("too high")
    elif int(user_input) < answer:
        print("too low")
    else:
        print("Correct")
        print(f"you need {count} guesses to find the answer")

