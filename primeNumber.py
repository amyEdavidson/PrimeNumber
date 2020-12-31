print("Please provide a single digit")
x = input()
x = int(x)

def isprime(x):
    if x > 1:
        if (x % 2) == 0:
            print(x,"is not a prime number")
        else:
            print(x,"is a prime number") 
    else:
        print(x,"is not a prime number")

isprime(x)