from datetime import datetime

registrations = []
print("   CAMPUS-X LIVE REGISTRATION")

while True:
    name = input("\nEnter Student/Company Name (or 'exit' to stop): ").strip().title()
    
    if name.lower() == 'exit':
        break
    
    current_time = datetime.now().strftime("%I:%M:%S %p | %d-%m-%Y")
    
    entry = {
        "id": len(registrations) + 1,
        "name": name,
        "time": current_time
    }
    
    registrations.append(entry)
    print(f"Success! {name} registered at {current_time}")

print("\n" + "="*45)
print(f"{'ID':<5} | {'NAME':<20} | {'TIMESTAMP'}")
print("-" * 45)

for r in registrations:
    print(f"{r['id']:<5} | {r['name']:<20} | {r['time']}")
