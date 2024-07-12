word1 = input("Enter a string1:")
word2 = input("Enter a string2:")

if(sorted(word1) == sorted(word2)):
    print(True)
else:
    print(False)