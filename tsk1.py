import time

a, b = (input()).split()
t = time.time_ns()
a, b = int(a), int(b)

print(a + b)

print(time.time_ns()-t)