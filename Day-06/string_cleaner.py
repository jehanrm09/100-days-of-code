text=input("Enter Statement: ")
alpha="AEIOU"
counter=0
new_text=""

for i in text:
    if i.isalpha():
        if i in alpha.lower() or i in alpha.upper():
            counter+=1
            continue
        else:
            new_text+=i
    elif i.isspace():
        new_text+=i
    else:
        continue

print("--- Analysis Complete ---")
print(f"Vowels found: {counter}")
print(f"Text without vowels: {new_text}")
