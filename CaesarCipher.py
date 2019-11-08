_in = input("[Message To Encrpyt]:")

Base = lambda x : ord('A') if x < ord('Z') else ord('a')
Shift = lambda x, y: chr((x - Base(x) + y) % 26 + Base(x))
ret = list(''.join(list(Shift(ord(ch), i) for ch in _in)) for i in range(0,26))

print("\n", ret, "\n")
print("[end]")
