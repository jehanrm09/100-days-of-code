print("--- User Database Report ---")
try:
    f=open("user.txt","r")
    for line in f:
        words=line.strip()
        print(words)
        parts= line.split(",")
        name = parts[0]
        age = parts[1]
        role = parts[2]
        print(f"Name: {name} | Age: {age} | Role: {role}",end="")
    
except FileNotFoundError:
    print("File Not Found")
