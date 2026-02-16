system_name = "CampusX Admin Dashboard"
max_capacity= 20

database = [
    {"name": "Tech Corp", "industry": "IT"},
    {"name": "HealthPlus", "industry": "Healthcare"},
    {"name": "DataFlow", "industry": "IT"},
    {"name": "GreenBuild", "industry": "Manufacturing"}
]

def show_dashboard():
    total_count = len(database)
    remaining = max_capacity - total_count
    
    it_count = 0
    for record in database:
        if record["industry"] == "IT":
            it_count += 1

    print(f"Total Registrations:  {total_count} / {max_capacity}")
    print(f"Remaining Slots:  {remaining}")
    print(f"IT Sector Share:  {it_count} companies")
    
    occupancy = (total_count / max_capacity) * 100
    print(f"Capacity Usage:  {occupancy}%")

show_dashboard()