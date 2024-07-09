"""Task 9 - Take a string and returns the number of words in it"""
sentence = "Guvi Geeks Networks Prrivated Limitted"
words = 0
for i in sentence:
    if i == " " or i == "\t" or i == "\n":
        words += 1
if len(sentence) > 0:
    print("Number of words:", words + 1)
else:
    print("Number of words: 0")