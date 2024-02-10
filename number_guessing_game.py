import random
while True:
    num = random.randint(1, 100)
    guesses = 0
    low = 1
    high = 100

    user = 0
    while user != num:
        user = int(input(f"Guess a number between {low} and {high}: "))
        if user > num:
            print("Too high")
            guesses += 1
            high = user
        elif user < num:
            print("Too low")
            guesses += 1
            low = user
        else:
            print("You got it!")
            guesses += 1
            print(f"You guessed {guesses} times.")
    startover = input("Play again? ")
    if startover == "yes":
        True
    else:
        print("Goodbye!")
        break