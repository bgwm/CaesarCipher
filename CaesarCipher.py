_in = input("[Message To Encrpyt]:")

'''
Calculate the start digit on ASCII as 'Base', based on 
lower case or captial case.
'''
Base = lambda x : ord('A') if x < ord('Z') else ord('a')


'''
Loop characters with lower case letter if the target letter 
is lower case, as well as captial case. function control the 
loop that the letter ASCII digit not overflow to no-letter 
characters.
'''
Shift = lambda x, y: chr((x - Base(x) + y) % 26 + Base(x))


'''
Straight forward of Caesar Cipher algorithm
'''
ret = list(''.join(list(Shift(ord(ch), i) for ch in _in)) for i in range(0,26))


print("\n", ret, "\n")
print("[end]")
