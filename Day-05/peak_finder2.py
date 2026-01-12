hieght=eval(input("Enter List of heights :"))
print(f"Scannning mountain range {hieght}")
peak=hieght[0]
indx=0
for i in range(len(hieght)):
    if peak<hieght[i]:
        print(f"New peak found: {hieght[i]} at position {i}")
        indx=i
        peak=hieght[i]
        continue

print(f"--- Analysis Complete ---")
print(f"highest Peak: {peak} meters \nLocated at Index:{indx}")