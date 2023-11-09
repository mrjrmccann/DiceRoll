import random

def roll_dice(num_dice):
    results = [str(random.randint(1, 6)) for _ in range(num_dice)]
    return " | ".join(results)

def main():
    print("Welcome to the Dice Game!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (or 0 to exit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if num_dice == 0:
            print("Thanks for playing! Goodbye!")
            break
        elif num_dice < 0:
            print("Please enter a positive number of dice.")
        else:
            dice_result = roll_dice(num_dice)
            print(f"Result of rolling {num_dice} dice: {dice_result}")

main()
