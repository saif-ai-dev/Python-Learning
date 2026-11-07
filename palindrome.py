name = (input("Enter a word: "))
reverse_word = name[::-1]

if(name == reverse_word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")