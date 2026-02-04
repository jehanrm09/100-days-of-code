print("--- Data Sanitizer ----")
name=input("Enter Full Name: ")
college=input("Enter College Name: ")

new_name=name.strip().title()
new_college=college.replace(",","-").strip().title()

print(f"ORIGINAL: {name} | {college}")
print(f"CLEANED: {new_name} | {new_college}")