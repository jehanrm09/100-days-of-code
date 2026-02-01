
password = "Student@123"
attempts = 3
flag = False 

print("--- SECURE TERMINAL  ---")

while attempts > 0:

    user_input = input(f"Enter Password: ").strip()
    if user_input == password:
        flag = True
        break  
    else:
        attempts -= 1
        print(f"Incorrect. {attempts} attempts left.")

if flag:
    print("ACCESS GRANTED!")
else:
    print("SYSTEM LOCKED: Too many failed attempts.")