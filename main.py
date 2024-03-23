import random

def guess_the_number():
    print("Welcome to Guess the Number game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        print(secret_number)
        guess = int(input("Enter your guess (between 1 and 100): "))

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

def multiplication_table():
    print("Let's practice multiplication tables!")
    num = int(input("Enter a number to generate its multiplication table: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Congratulations! You win!")
    else:
        print("Oops! Computer wins!")

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def list_primes():
    print("Prime numbers between 1 and 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")

def main():
    print("Welcome to Fun with Python!")
    while True:
        print("\nChoose an option:")
        print("1. Guess the Number")
        print("2. Multiplication Table")
        print("3. Rock, Paper, Scissors")
        print("4. List Prime Numbers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            multiplication_table()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            list_primes()
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
