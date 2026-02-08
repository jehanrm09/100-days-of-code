print("--- Student System ---")

try:
    with open("students.txt", "r") as f:
        data = f.read().split()
        print(f"System Ready. {len(data)} records loaded.")

except FileNotFoundError:
    print("Database missing. Creating a new 'students.txt'...")
    with open("students.txt", "w") as f:
        f.write("") 
    data = []

except PermissionError:
    print("ERROR: The file is open in another program. Please close it and restart.")
    data = []

print(f"Current Session Count: {len(data)}")