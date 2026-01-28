with open("work_task.txt","w") as f1:
    f1.write("Create new textfile\n")
    f1.write("Add text in textfile\n")
    f1.write("close the textfile")

with open("personal_task.txt","w") as f2:
    f2.write("I am 2nd Year Computer Engineering Student\n")
    f2.write("I’m currently on a journey to explore the vast world\n")
    f2.write("I love meeting new people\n")

files_to_merger=["work_task.txt","personal_task.txt"]

with open("master_log.txt","w") as f:
    try:
        for i in files_to_merger:
            print(f"Merging: {i}... Success!")
            f3=open(f"{i}")
            f.write(f3.read())
            
    except FileNotFoundError:
        print(f"Merging: {i}... Error: File not found.")
print()
print("--- Process Complete ---\nCheck 'master_log.txt' for the combined results.")