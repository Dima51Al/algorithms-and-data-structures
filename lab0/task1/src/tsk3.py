a, b = open("../txtf/input.txt").read().split()
a, b = int(a), int(b)

open("../txtf/output.txt", "w").write(str(a + b))

