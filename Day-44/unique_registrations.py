def count_unique_registrations(names):
    
    unique_names = set()
    
    for name in names:
        clean_name = name.strip().lower()
        unique_names.add(clean_name)
        
    return len(unique_names)

test_data = ["Google", " google ", "GOOGLE", "Microsoft", "microsoft", "Apple"]

result = count_unique_registrations(test_data)
print(f"Total Unique Companies: {result}")