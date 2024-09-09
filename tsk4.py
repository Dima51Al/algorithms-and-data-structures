a, b = open("input.txt").read().split()
a, b = int(a), int(b)

open("output.txt", "w").write(str(a+b**2))