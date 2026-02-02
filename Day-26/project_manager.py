print("--- Project Manager ---")
print("1. Run System Audit\n2. Write Quick Note\n3. Exit")
print()
while True:
    choice=input("Select an option (1-3): ")
    if choice=="3":
        print("Shutting down. Goodbye!\n")
        break

    elif choice=="2":
        note=input("Enter your Note: ")
        f=open("Notes.txt","a")
        f.write(note)
        print("Note saved successfully.\n")

    elif choice=="1":
        print("All systems operational.\n")

    else:
        print("Invalid choices. Re-enter\n")