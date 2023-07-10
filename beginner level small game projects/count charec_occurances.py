def count_charcs(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1

        else:
            counts[c] = 1

    return counts


s = input('enter the sting for count here')
counts = count_charcs(s)
for c, counts in counts.items():
    print(f"{c}: {counts}")
