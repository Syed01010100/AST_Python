"""1.Write a Python program to calculate the total number of Vowels and Count of each
individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited" ?"""

text = "Guvi Geeks Network Private Limited"
text_lower = text.lower()
vowel = "aeiou"
d = {}. fromkeys(vowel, 0)
count = 0
for charactor in text_lower:
    if charactor in vowel:
        count+= 1
print("Total number of Vowels:", count)
for i in text_lower:
    if (i in d):
        d[i] = d[i] +1
print("Count of each individual vowel:",d)

