a = int(input())
t1 = 1
t2 = 1
t3 = 0
while t3 < a:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
if t3 == a:
    print("Это число Фибоначчи!")
else:
    print("Это НЕ число Фибоначчи.")
