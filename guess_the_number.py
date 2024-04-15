secret_number = 18

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

print("You will get total 10 attempts. Good luck!")

attempts = 0

while attempts < 10:
    attempts += 1
    print(f"\nAttempt {attempts}")
    number = int(input("Enter the secret number: "))

    if attempts == 10:
        print("\nGame Over! You don't have any more attempts left")
        break

    if number > secret_number:
        print("The secret number is smaller than the number you entered.")
        print(f"You still have {10 - attempts} attempts left. Try again!")

    elif number < secret_number:
        print("\nThe secret number is larger than the number you entered.")
        print(f"You still have {10 - attempts} attempts left. Try again!")

    elif number == 18:
        print(f"\nCongratulations muggle! You found my secret number in {attempts} attempts")
        print("My secret number is:", secret_number)
        break
