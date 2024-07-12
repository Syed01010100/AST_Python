# Create a Pyramid of Numbers from 1 to 20 using For loop?
num = int(20) # Value given by integer so used int.
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()