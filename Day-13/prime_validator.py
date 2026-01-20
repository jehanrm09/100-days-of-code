def is_prime(num):
    if num<2:
        return False
    
    for j in range(2,num):
        if num%j==0:
            return False
        
    return True

number=eval(input("Enter list of numbers: "))

print("--- Prime Number Analysis ---")
for i in number:
    if is_prime(i):
        print(f"✅ {i} is a Prime Number.")

    else:
        print(f"❌ {i} is NOT a Prime Number.")



