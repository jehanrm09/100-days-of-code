def find_discount_pair(id_list, required_sum):
    id_memory = {}

    for current_pos, current_id in enumerate(id_list):
        needed_id = required_sum - current_id
        
        if needed_id in id_memory:
            previous_pos = id_memory[needed_id]
            print(f"✨ Match Found! ID {needed_id} and ID {current_id} work together.")
            return [previous_pos, current_pos]

        id_memory[current_id] = current_pos

    return "No matching pair found."

daily_ids = [102, 305, 204, 150, 99, 200]
winning_total = 400 
target = 404

result = find_discount_pair(daily_ids, target)
print(f"Indices of the winning IDs: {result}")