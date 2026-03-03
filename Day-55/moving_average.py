def moving_average(nums, k):

    result = []
    current_window_sum = 0
    
    w = []

    for i in range(len(nums)):
        w.append(nums[i])
        current_window_sum += nums[i]

        if len(w) > k:
            oldest = w.pop(0)
            current_window_sum -= oldest
            
        if len(w) == k:
            result.append(current_window_sum / k)
            
    return result

data = [1, 10, 3, 5, 6, 7]
size = 3

averages = moving_average(data, size)
print(f"Moving Averages: {averages}")