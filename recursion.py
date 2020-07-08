from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(number):
    if type(number) != int:
        raise TypeError("number - must be a positive int !")
    if number < 1:
        raise ValueError("number - must be a positive int !")

    # Compute the Nth term
    if number == 1:
        return 1
    elif number == 2:
        return 1
    elif number > 2:
        return fibonacci(number-1) + fibonacci(number-2)


scope = int(input("Range to be calculated: "))
for number in range(1, scope):
    print(fibonacci(number))
