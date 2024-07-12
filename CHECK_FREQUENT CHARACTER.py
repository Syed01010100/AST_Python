# Write a program that takes a string and returns the most frequent character in it.
string = "Guvi Geeks Network Private Limited"
string = "".join(string.split())
count = {}
for letter in string:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1
max_key = max(count, key=count.get)
print("String : ", string)
print(f"Character : {max_key} has frequent character in it in NO. : {count[max_key]}")