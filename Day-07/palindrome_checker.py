text=input("Enter input: ")
new_text=""
reverse_text=""

for i in text:
    if i.isalnum():
        new_text+=i.lower()

    elif i.isspace():
        continue

    continue

for i in range( len(new_text)-1 , -1 , -1):
    reverse_text=reverse_text+new_text[i]

print("-- Result --")
print(f"Original (Cleaned): {new_text}")
print(f"Reversed: {reverse_text}")
if new_text == reverse_text:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")