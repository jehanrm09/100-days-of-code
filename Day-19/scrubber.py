target = "secret"
replacement = "[REDACTED]"

try:
    with open("note.txt", "r") as file:
        lines = file.readlines()

    cleaned_lines = []
    for i in lines:
        new_line = i.replace(target, replacement)
        cleaned_lines.append(new_line)

    with open("note.txt", "w") as file:
        file.writelines(cleaned_lines)
        
    print(f"Success! All instances of '{target}' have been hidden.")

except FileNotFoundError:
    print("Error: notes.txt doesn't exist. Run your Day 16 script first!")
