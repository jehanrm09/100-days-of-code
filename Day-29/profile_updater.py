f= open("students.txt","r")
data=f.read().split()

print("--- Profile Updater ---")
name=input("Enter Name Of Student To Update: ").strip().title()

found=False
for i in range(0, len(data)):
    if name in data:
        new_data=input("Enter New Data: ").strip().title()
        data[i]=new_data

        found=True
        break

    else:
        print("Student Not Found.")
        name=input("Re-enter Name Of Student To Update: ").strip().title()

if found:
    with open("students.txt","w")  as f1:
        for i in data:
            f1.write(i +"\n")
    print("Updated Successfully!")       

else:
    print("Student Not Found.")