# The Problem: You need to find the "Power Level" of a system. You are given a Target Number, and you must write a loop that starts at 1 and squares every number (n^2) until it either hits the target exactly or surpasses it
user_input=int(input("Enter target value to find perfect root:"))
n=1
print(f"---Searching for perfect root of {user_input}---")
while(n*n)<=user_input:
    if user_input==(n*n):
        print(f"SUCCESS: {n} * {n} = {n*n}")
        print(f"target found at root {n}")
        break
    n+=1
else:
    closest=(n-1)**2
    print(f"No perfect root found. the closet square below it was {closest}")
    print(f"Search completed after {n-1} iteration.")
