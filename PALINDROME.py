# Write a program that takes a string and returns True if it is a palindrome, False otherwise.
def is_palindrome(text):
    lenght = len(text)
    for i in range(0, lenght // 2):
        if (text[i] != text[lenght-i-1]):
            return False
    return True
string1 = "mom"
print(is_palindrome(string1))
string2 = "syed"
print(is_palindrome(string2))