# While loop
i = 1
while i <= 5:
    print("i:", i)
    i += 1

# While loop with break
j = 1
while j <= 5:
    if j == 3:
        break
    print("j:", j)
    j += 1

# While loop with continue
k = 0
while k < 5:
    k += 1
    if k == 3:
        continue
    print("k:", k)
