f=open("students.txt","r")
data=f.read().split()

name=input("Enter Name Of The Student To Remove: ").strip().title()
updated_data=[student for student in data if name not in student] 

if len(data) > len(updated_data):
    with open("students.txt","w") as f1:
        for i in updated_data:
            f1.write(i+"\n")
    print(f"'{name}' has been removed.")
    print("New Data Updated.")
else:
    print("Data Not Found.")