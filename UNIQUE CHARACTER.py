# Write a program that takes a string and returns the number of unique characters in it
string = "Guvi Geeks Network Private Limited"
dictionary = {}
for i in string:
    dictionary[i]=0
for i in string:
    dictionary[i]=dictionary[i]+1
print(dictionary)
for i in  string:
    if(dictionary[i]==1):
        print(i)
    