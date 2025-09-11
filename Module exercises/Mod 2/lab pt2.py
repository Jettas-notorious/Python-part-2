word=input("Enter a word:")
word=word.replace(" ","")
if len(word)>1 and word.upper()==word[::-1].upper():
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    