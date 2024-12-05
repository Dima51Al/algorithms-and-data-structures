def H(v):
    A = 40
    p = 31
    return (A * (v % p)) % 9


print(H(2))
