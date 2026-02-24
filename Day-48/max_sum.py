def find_peak_3_days(daily_counts):
    k = 3
    
    if len(daily_counts) < k:
        return "Not enough data for a 3-day window!"

    current_window_sum = sum(daily_counts[:k])
    max_registrations = current_window_sum
    
    for i in range(k, len(daily_counts)):
        current_window_sum += daily_counts[i] - daily_counts[i - k]
        
        if current_window_sum > max_registrations:
            max_registrations = current_window_sum
            
    return max_registrations

registrations = [5, 12, 3, 10, 8, 15, 2] 

peak = find_peak_3_days(registrations)
print(f"The highest 3-day registration total was: {peak}")