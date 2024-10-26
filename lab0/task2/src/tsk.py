def fib(noun) -> int:
    if noun < 0:
        return -1
    if noun == 0:
        return 0
    tmp1, tmp2 = 1, 1
    if noun == 1 or noun == 2:
        return 1
    number = 2
    while number != noun:
        key = tmp1
        tmp1 = tmp1 + tmp2
        tmp2 = key
        number += 1
    return tmp1
