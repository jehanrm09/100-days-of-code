data = "LJ University,Engineering,Ahmedabad,2026"
parts = data.split(",")

student_profile = {
    "college": parts[0],
    "stream": parts[1],
    "location": parts[2],
    "batch": parts[3]
}

print("--- SYSTEM PROFILE ---")
print(f"College: {student_profile['college']}")
print(f"Location: {student_profile['location']}")
print(f"Graduation: {student_profile['batch']}")

student_profile["status"] = "Active"