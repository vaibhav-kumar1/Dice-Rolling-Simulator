#Dice Rolling Simulator : Create a program that simulates rolling a pair of dice and prints out the results
import random
import time

def roll_dice():
    dice = [1, 2, 3, 4, 5, 6]
    dice1 = random.choice(dice)
    dice2 = random.choice(dice)
    return dice1, dice2

def display_dice(dice1, dice2):
    print("\nRolling the dice...")
    time.sleep(1)
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")

def main():
    while True:
        print("--- Dice Rolling Simulator ---")
        input("Press Enter to roll the dice...")

        dice1, dice2 = roll_dice()
        display_dice(dice1, dice2)

        choice = input("\nDo you want to roll the dice again? (y/n): ")
        if choice.lower() != "y":
            break

    print("\n--- Thank you for using the Dice Rolling Simulator! ---")

if __name__ == "__main__":
    main()
