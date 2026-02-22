def is_valid_registration_key(s):

    left = 0
    right = len(s) - 1
    
    while left < right:

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

key_1 = "A man, a plan, a canal: Panama"
key_2 = "race a car" 
key_3 = "No 'x' in Nixon"

print(f"Key 1 Valid: {is_valid_registration_key(key_1)}")
print(f"Key 2 Valid: {is_valid_registration_key(key_2)}")
print(f"Key 3 Valid: {is_valid_registration_key(key_3)}")