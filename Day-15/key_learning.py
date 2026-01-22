data = ["Alice@gmail.com", "Bob123", "CHARLIE@HOTMAIL.COM", "Admin", "support@company.com"]

email_data=[]
email_data=[email.lower() for email in data if ".com" in email.lower()]

print("--- Raw Data Analysis ---")
print(f"Original: {data}\n")

print("--- Cleaned Email List ---")
print(email_data)