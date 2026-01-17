inventor={"apple": 50,
    "banana": 30,
    "orange": 80,
    "milk": 25,
    "bread": 35}

print(" --- Welcome to the store ---")
print("Available : ",end=" ")
for i in inventor.keys():
    print(i,end=" ")

print()
while(True):
    item_name=input("Enter item name to check price (or 'q' to quit): ").lower()
    if item_name=="q":
        print("Closing System.")
        break
    elif item_name in inventor:
        print(f"The price of {item_name} is {inventor[item_name]}")
    else:
        print(f"Error: '{item_name}' is not in our inventory.")
        