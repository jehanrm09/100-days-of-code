database = [
    {"id": 1, "name": "Alex", "time": "10:00 AM"},
    {"id": 3, "name": "John", "time": "11:30 AM"},
    {"id": 2, "name": "Priya", "time": "10:45 AM"}
]

newest_first = sorted(database, key=lambda x: x['id'], reverse=True)

alphabetical = sorted(database, key=lambda x: x['name'])

print("\n--- NEWEST REGISTRATIONS FIRST ---")
for r in newest_first:
    print(f"ID {r['id']}: {r['name']} ({r['time']})")

print("\n--- ALPHABETICAL LIST ---")
for r in alphabetical:
    print(f"• {r['name']}")