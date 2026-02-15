system_name= "CampusX Student Portal"
max_capacity = 5
valid_industries = ["IT", "Manufacturing", "Finance", "Healthcare"]

database = [{"name": "Alex"}, {"name": "Priya"}, {"name": "John"}]

print(f"--- Welcome to {system_name} ---")

def check_availability():
    if len(database) >= max_capacity:
        print("REGISTRATION FULL: Maximum capacity reached.")
        return False
    return True

print("\nAvailable Industries:")
for i, industry in enumerate(valid_industries, 1):
    print(f"{i}. {industry}")

if check_availability():
    new_name = input("\nEnter Company Name: ").strip().title()
    print("Registration Open. Please proceed...")