readings=[12,45,67,23,89,34,99,10,56]
threshold = 60
alert =[]
print(f"Analyzing {len(readings)} sensor readings...")
for i in range(0,len(readings)):
    if(readings[i]>threshold):
        print(f"ALERT : High value detected :{readings[i]}")
        alert.append(readings[i])
    continue

print("---Analysis Completed---")
print(f"Total Alert Found: {len(alert)}")

if len(alert) > 0:
    avg= sum(alert)/len(alert)
    print(f"Average Alert Severity : {avg}")