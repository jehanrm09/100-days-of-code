def longest_string(text):
    seen_at = {}
    
    max_length = 0
    start_point = 0 
    for current, char in enumerate(text):

        if char in seen_at and seen_at[char] >= start_point:
          start_point = seen_at[char] + 1
        
        seen_at[char] = current
        
        current_stretch_length = current - start_point + 1
        
        if current_stretch_length > max_length:
            max_length = current_stretch_length
            
    return max_length

test_1 = "abcabcbb"
test_2 = "pwwkew"
test_3 = "ganpatuniversity"

print(f"Longest clean stretch in '{test_1}': {longest_string(test_1)}")
print(f"Longest clean stretch in '{test_2}': {longest_string(test_2)}")