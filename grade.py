marks = int(input("Enter your percentage: "))

if (marks >= 90):
    print("Grade A")
elif(marks >= 70 and marks < 90):
    print("Grade B")
elif(marks >= 45 and marks < 70):
    print("Grade C")
else:
    print("Grade D")