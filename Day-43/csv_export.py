students = [
    ["Alex", "Ganpat Uni", "17-Feb"],
    ["Priya", "PDPU", "18-Feb"],
    ["John", "LJU", "19-Feb"]
]

f= open("manual_report.csv", "w")
f.write("Student Name, University, Date\n")

for s in students:
        row = f"{s[0]},{s[1]},{s[2]}\n"
        f.write(row)


print("'manual_report.csv' created.")