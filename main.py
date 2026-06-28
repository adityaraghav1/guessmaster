import random

print("Welcome to GuessMaster!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

guess = int(input("Enter your guess: "))
attempts = 1

while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low 📉. Try again!")
        else:
            print("Your guess is too high 📈. Try again!")

        guess = int(input("Enter your guess: "))
        attempts += 1

print("🎉 Congratulations!")
print(f"You guessed the number in {attempts} attempts.")
