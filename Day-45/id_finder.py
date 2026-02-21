def find_first_unique(batch_id):

    char_count = {}
    
    for char in batch_id:
        char_count[char] = char_count.get(char, 0) + 1
    
    for index in range(len(batch_id)):
        if char_count[batch_id[index]] == 1:
            return index
            
    return -1

id_1 = "ganpatuniversity"
id_2 = "aabbcc"     
id_3 = "lovelypython"

print(f"Test 1 Index: {find_first_unique(id_1)}") 
print(f"Test 2 Index: {find_first_unique(id_2)}")
print(f"Test 3 Index: {find_first_unique(id_3)}")