import os
file_to_move="master_log.txt"
print("Checking workspace...")

if os.path.exists("Archive"):
    print("Folder already exists, skipping...")
else:
    print("Folder 'Archive' not found. Creating it now...")
    os.mkdir("Archive")
    print("Success! Folder created.")

if os.path.exists(file_to_move):
    print(f"moving '{file_to_move}' to 'Archive/'...")
    new_location=os.path.join("Archive",file_to_move)
    os.rename(file_to_move,new_location)
    
else:
    if os.path.exists(new_location):
        print(f"The file is already safely inside 'Archive'.")
    else:
        print(f"Error: '{file_to_move}' not found. Did you run Day 21?")

print("Workspace is now organized!")