def is_syntax_valid(code_string):
    stack = []
    
    mapping = {")": "(", "}": "{", "]": "["}

    for char in code_string:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return len(stack) == 0

test_1 = "{[()]}"
test_2 = "{[(])}"
test_3 = "((()))"

print(f"Test 1 Valid: {is_syntax_valid(test_1)}")
print(f"Test 2 Valid: {is_syntax_valid(test_2)}")
print(f"Test 3 Valid: {is_syntax_valid(test_3)}")