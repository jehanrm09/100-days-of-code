f=open("note.txt")
line_count=0
line=f.readlines()
f.seek(0)
word_count=f.read().split()
f.seek(0)
char_count=len(f.read())-(len(word_count)-1)

for i in line:
    line_count+=1

print(line_count)
print(len(word_count))
print(char_count)
