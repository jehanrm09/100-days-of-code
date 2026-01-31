print("--- Secure System Portal ---")
stored_pass="Student@123"
admin_user="admin_zeh"

age=int(input("Enter Your age: "))
user=input("Enter Your Username: ").lower()
password=input("Enter Your Password: ")

if stored_pass==password and(age>=18 or user==admin_user):
    print("\n Welcome to secure area.")

    if user==admin_user:
        print("Logged as Admin")
        
else:
    print("Access Denied")

    if password!=stored_pass:
        print("Incorrect Password.")
    else:
        print("Age requirements not met.")