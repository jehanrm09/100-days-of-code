f=open("note.txt")
line_count=0
line=f.readlines()
f.seek(0)
word_count=f.read().split()
f.seek(0)
char_count=len(f.read())-(len(word_count)-1)

for i in line:
    line_count+=1

print("--- File Statistics Report ---")
print(f"Total Lines: {line_count}")
print(f"Total Words:: {len(word_count)}")
print(f"Total Characters: {char_count}")
