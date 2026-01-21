def calculate_stuff(length=4,width=5):
    area=length*width
    peri=2*(length+width)

    return area,peri

length=float(input("Enter length: "))
width=float(input("Enter Widht: "))

print()
print("--- Rectangle Analysis ---\n")

area1,peri1=calculate_stuff(length,width)
print(f"Scenario 1: Custom Dimensions (Length={length}, Width={width})\nArea: {area1}\nPerimeter: {peri1}\n")

area2,peri2=calculate_stuff(length)
print(f"Scenario 2: Default Width (Length={length})\nArea: {area2}\nPerimeter: {peri2}\n")

a,p=calculate_stuff(length=15,width=10)
print(f"Scenario 3 (15x10): \nArea = {a}, \nPerimeter = {p}")