list_a = [10, 20, 30, 40, 50, 20, 10]
list_b = [30, 40, 50, 60, 70, 40]

created_set = set(list_a)

intersection = []

for item in list_b:
    if item in created_set:
        intersection.append(item)
        created_set.remove(item)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"✅ Common Elements Found: {intersection}")