hieght=eval(input("Enter List of heights :"))
print(f"Scannning mountain range {hieght}")
peak=0
indx=0
for i in range(1,len(hieght),2):
    if hieght[i-1]>hieght[i]:
        print(f"New peak found: {hieght[i-1]} at position {i-1}")
        indx=i-1
        peak=hieght [i-1]
        continue
    elif hieght[i-1]<hieght[i]:
        print(f"New peak found: {hieght[i]} at position {i}")
        indx=i
        peak=hieght [i]
        continue
    else:
        continue
print(f" --- Analysis Complete --- ")
print(f"highest Peak: {peak} meters \nLocated at Index:{indx}")
