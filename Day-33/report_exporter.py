students = ["Aakib | Ganpat", "Priya | LJIET", "John | PDPU", "Dua | Ganpat"]
colleges = ["Ganpat", "PDPU", "LJIET"]

with open("final_report.txt", "w") as f:
    
    f.write("=== OFFICIAL STUDENT DISTRIBUTION REPORT ===\\n")

    for college in colleges:
        f.write(f"COLLEGE: {college}\n")
        
        for i in students:
            if college in i:
                name = i.split("|")[0].strip()
                f.write(f"  > {name}\n")
        
        f.write("\n") #

print("-Open 'final_report.txt' to see the result.")