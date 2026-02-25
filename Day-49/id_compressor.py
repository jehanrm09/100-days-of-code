def compress_id(raw_id):
    if not raw_id:
        return ""

    compressed = []
    count = 1
    
    for i in range(1, len(raw_id)):
        if raw_id[i] == raw_id[i - 1]:
            count += 1
        else:
            compressed.append(raw_id[i - 1] + str(count))
            count = 1
            
    compressed.append(raw_id[-1] + str(count))
    
    result = "".join(compressed)
    
    return result if len(result) < len(raw_id) else raw_id

id_1 = "AAAAABBBCC"
id_2 = "ABC"
id_3 = "GGGGRRRXXXXX"

print(f"Original: {id_1} -> Result: {compress_id(id_1)}")
print(f"Original: {id_2} -> Result: {compress_id(id_2)}")
print(f"Original: {id_3} -> Result: {compress_id(id_3)}")