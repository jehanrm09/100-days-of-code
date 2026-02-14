data=[{"name":"Rahul","college":"LJU","skill": "Python"},
      {"name": "Priya", "college": "PDEU", "skill": "Web Dev"},
      {"name": "Dua", "college": "Nirma", "skill": "Java"}]

user_input=input("Enter Name Of The Student To Remove: ").strip().title()

updated_data= [student for student in data if student['name'] != user_input]
if len(data) > len(updated_data):
    data=updated_data
    print(f"{user_input} has been removed.")
else:
    print("DATA NOT FOUND.")

print("-:CURRENT DATABASE:-")
for i in data:
    print(i)