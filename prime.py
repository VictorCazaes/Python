def prime(num):
    if num > 1 and not isDivisible(num):
        print(str(num) + " is prime")
    else:
        print(str(num) + " isn't prime")


def isDivisible(num):
    for i in range(2, num):
        if (num % i) == 0:

            return True

    return False
