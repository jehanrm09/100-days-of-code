def is_prime(num):
    number=int(input("Enter Number: "))
    if number<2:
        return False
    
    for i in(2,num):
        if num%i==0:
            return False
    return True

