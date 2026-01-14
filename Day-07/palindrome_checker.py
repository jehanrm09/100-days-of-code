text=input("Enter input: ")
new_text=""
reverse_text=""

for i in text:
    if i.isalnum():
        new_text+=i.lower()

    elif i.isspace():
        continue

    continue

