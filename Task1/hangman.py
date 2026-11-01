import random

while True:

    with open('wordlist.txt', 'r') as file:
        words = file.read().splitlines()


        a = random.choice(words)

        print("Welcome to Hangman!")

        attempts = 6
        won = False

        rn = random.randint(0, len(a) -1)

        f = a.strip()

        a = list(f)

        letter = a[rn]
        a[rn] = "_"
        
        print("".join(a))

        while attempts > 0:
            guess = input("Guess a letter: ").lower()

            if guess == letter:
                print("you won")
                print("you want to play again? (y/n)")
                play_again = input().lower()
                if play_again == 'n':
                    exit(0)
                else:
                    print("Thanks for playing!")
                break
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
                if attempts == 0:
                    print(f"You lost! The correct letter was '{letter}'.")
                    break




