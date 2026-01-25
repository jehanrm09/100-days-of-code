word=input("Enter search keyword: ")
f=open("note.txt")
lines=f.readlines()
flag=False

print("--- Search Results ---")
for index,line in enumerate(lines,start=1):
   if word in line:
      flag=True
      print(f"Line {index} - {line}")

if flag==False:
    print(f"No matches found for {word}.")
    
