# Write a program that takes a string and returns a new string with all the vowels removed.
string = input("Enter a string:")
vowel = "aeiouAEIOU"
result = ""
for charactor in string:
    if charactor not in vowel:
        result+=charactor
print(result)