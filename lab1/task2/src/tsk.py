def f(n):
    if n == 0:
        return 0
    s1, s2 = 1, 1
    if n == 1 or n == 2:
        return 1
    c = 2
    while c!=n:
        k = s1
        s1 = s1+s2
        s2 = k
        c+=1
    return s1
s = f(int(open("input.txt").read()))
open("output.txt", "w").write(str(s))
