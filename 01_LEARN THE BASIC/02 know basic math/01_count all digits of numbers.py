def countdigits(n):
    if n == 0:
        return 1
    Nodigits = 0
    while n > 0:
        n = n // 10
        Nodigits += 1
    return Nodigits

if __name__ == "__main__":
    n = 345364
    print("The number is :",n)
    print("The number of digits in the given number: ",countdigits(n))