# This is an assignment to write a program that tells if  aphabet entered is a vowel or consonant
while True:
    alphabet = input("enter a single aphabet : ").lower()
    if len(alphabet) != 1 or len(alphabet) != alphabet.isalpha():
        print("invalid! please, enter a single alphabet")
        continue
    if alphabet in ["a","e","i","o","u"]:
        print(f"{alphabet} is a vowel")
    else:
        print(f"{alphabet} is a consonant")
    break