data=[]

data.append({"name":"Rahul","college":"LJU","field":"CE"})
data.append({"name": "Priya", "college": "PDEU", "field": "Civil"})
data.append({"name": "Dua", "college": "Nirma", "field": "IT"})

print(f"--- Total Record {len(data)}---")
count=0
for i in data:
    print(f"Student: {i['name']} | Department: {i['field']}")

    if "LJU" in i['college']:
        count+=1

print(f"Total LJU Students: {count}")