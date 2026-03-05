def first_unique_char(s):
    char_counts = {}
    
    for i in s:
        char_counts[i] = char_counts.get(i, 0) + 1
    
    for index in range(len(s)):
        current_char = s[index]
        if char_counts[current_char] == 1:
            return index
            
    return -1

string_a = "leetcode"
string_b = "loveleetcode"
string_c = "aabb"

print(f"Result for 'leetcode': {first_unique_char(string_a)}")
print(f"Result for 'loveleetcode': {first_unique_char(string_b)}")
print(f"Result for 'aabb': {first_unique_char(string_c)}")