data=["apple", "banana", "apple", "orange", "apple", "banana", "grape"]
fruits={}

for i in data:
    if i in fruits:
        fruits[i]+=1
    else:
        fruits[i]=1

x=max(fruits.values())
print(x)

print(f"Processing Data:{data}")
print("--- Final Counts ---")
for i,j in fruits.items():
    print(f"{i}: {j}")
    if x == j :
        max1 = i

print("Most frequent item: " , max1)
