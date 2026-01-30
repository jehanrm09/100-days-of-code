import os
files=os.listdir()
counter=0

print("--- Scanning Workspace for Python Scripts ---")
for i in files:
    if i.endswith(".txt"):
        counter+=1
        print(f"Found: {i}")
    else:
        continue

print()
print(f"Total scripts identified: {counter}")