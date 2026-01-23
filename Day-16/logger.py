print("--- Daily Logger ---")
text=input("What did you accomplish today?")
f=open("note.txt","a")
f.write(text+"\n")

print("\n--- Note Saved! ---")

print("Current content of your notes:")
with open("note.txt", "r") as file:
    content = file.read()
    print(content)