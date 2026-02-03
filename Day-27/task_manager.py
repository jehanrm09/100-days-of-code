import os
filename="task.txt"
task=[]

if os.path.exists(filename):
    f=open(filename,"r")
    task=f.readlines()
    print("List Created")
else:
    print("File Not Found")

while True:
    print("\n--- Task Manager ---")
    print("1.View Task \n2.Add Task \n3.Remove Task \n4.Exit\n")
    choice=input("Enter Your Choice: ")

    if choice=="1":
        print("-: YOUR TASK :-")
        for i,tasks in enumerate(task,1):
            print(f"{i}. {tasks}",end="")

    elif choice=="2":
        user_input=input("Enter New Task: ")
        task.append(user_input)
        print("Task Added.")

    elif choice=="3":
        delet=int(input("Enter index number of Task you want to remove: "))
        del task[delet-1]
        print("Task Deleted.")

    elif choice=="4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.\n")