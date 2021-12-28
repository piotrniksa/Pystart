p_3 = set()
p_5 = set()

for t in range(0, 1000):
    if t % 3 == 0:
        p_3.add(t)

for r in range(0, 1000):
    if r % 5 == 0:
        p_5.add(r)

print(sorted(list(p_3 & p_5)))
