data=[{"name":"Rahul","college":"LJU","skill": "Python"},
      {"name": "Priya", "college": "PDEU", "skill": "Web Dev"},
      {"name": "Dua", "college": "Nirma", "skill": "Java"}]

print("--- Profile Modifier ---")
user_input=input("Enter Name Of The Student To Update: ").strip().title()
flag = False
for i in data:
    if i['name']==user_input:
        print(f"Current Skillof {i['name']}= {i['skill']}")
        new_skill=input("Enter new skill: ")

        i['skill']=new_skill

        print("UPDATED")
        flag=True
        break

if not flag:
    print("Not Found")

print("UPDATED DATA")
print(data)