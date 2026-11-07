score = 0

answer1 = input("What is the Capital of India:- ")

if answer1 == "delhi" or answer1 == "DELHI":
    print("Correct✅")
    score += 1
else:
    print("Wrong❌")

answer2 = input("Which planet is known as the Red Planet:- ")
if answer2 == "mars" or answer2 == "MARS":
    print("Correct✅")
    score +=1
else:
    print("Wrong❌")

answer3 = input("Which is the Largest continent in the World:- ")
if answer3 == "asia" or answer3 == "ASIA":
    print("Correct✅")
    score +=1
else:
    print("Wrong❌")

answer4 = input("Which is the Largest ocean in the World:- ")
if answer4 == "pacific" or answer4 == "PACIFIC":
    print("Correct✅")
    score +=1
else:
    print("Wrong❌")

answer5 = input("2 + 2 multiplied by 3 will be:-  ")
if answer5 == "12" or answer5 == "twelve" or answer5 == "TWELVE":
    print("correct✅")
    score +=1
else:
    print("Wrong❌")

print("Score is: ", score)