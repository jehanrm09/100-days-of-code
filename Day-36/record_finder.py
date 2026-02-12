data=[{"name":"Rahul","college":"LJU","field":"CE"},
      {"name": "Priya", "college": "PDEU", "field": "Civil"},
      {"name": "Dua", "college": "Nirma", "field": "IT"}]

print("--- Record Finder ---")
user_input=input("Enter Name To Search: ").strip().title()

flage=False
for student in data:
    if student['name'] == user_input:
        print("-: Record Founded :-")
        print(f"name: {student['name']}")
        print(f"college: {student['college']}")
        print(f"field: {student['field']}")
        found=True
        break

if not found:
    print(f"No Record Founded For{user_input} ")