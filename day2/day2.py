with open("day2.txt", "r") as file: lines = [line.split() for line in file.read().splitlines()]
def is_good(r): inc = dec = False; return all(abs(d := int(r[i]) - int(r[i+1])) <= 3 and d and not (d < 0 and dec) and not (d > 0 and inc) and (inc := d < 0 or inc) is not None and (dec := d > 0 or dec) is not None for i in range(len(r)-1))
safe = sum(is_good(r) for r in lines)
tolerance = sum(any(is_good(r[:n] + r[n+1:]) for n in range(len(r))) for r in lines if not is_good(r))
print(safe, tolerance, safe + tolerance)
