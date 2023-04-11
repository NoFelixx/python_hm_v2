from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    for x in range(1, n + 1):
        if x % 15 == 0:
            yield "fizz buzz"
        elif x % 3 == 0:
            yield "fizz"
        elif x % 5 == 0:
            yield "buzz"
        else:
            yield str(x)


print(fizzbuzz(20))
