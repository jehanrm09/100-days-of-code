size = 5
print(f"--- {size}*{size} multiplication table ---")
for i in range(1,size+1):
    for j in range(1,size+1):
        print(f"{i*j:3} ",end=" ")

    print()