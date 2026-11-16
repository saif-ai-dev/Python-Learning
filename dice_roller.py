import random

print("===== DICE ROLLER =====")

while True:
    roll = input("\nPress Enter to Roll the dice or type 'q' to quit: ")

    if roll.lower() == 'q':
        print("Thanks for Playing!")
        break

    dice = random.randint(1,6)
    print("You rolled:", dice)