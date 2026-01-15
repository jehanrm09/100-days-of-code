for i in range(1,51):
    if i%15==0:
        print(f"{i}: FizzBuzz Both 3 and 5")
    elif i%5==0:
        print(f"{i}: Buzz")
    elif i%3==0:
        print(f"{i}: Fizz")
    else:
        print(i)