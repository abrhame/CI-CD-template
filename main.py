def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    user_input = int(input("Please Enter integer: "))
    return(fizzbuzz(user_input))


if __name__ == "__main__":
    print(main())
