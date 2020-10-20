#!/usr/bin/env python3
from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

r = remote("140.112.31.97", 30000)

enc = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

def oracle(c):
    r.sendlineafter('cipher = ', c.hex())
    if b'YES' in r.recvline():
        return True
    else:
        return False

flag = b''
for i in range(16, len(enc), 16):
    ans = b''
    iv, block = enc[i-16:i], enc[i:i+16]
    for j in range(16):
        temp = b''
        f = 1 
        for k in range(256):
            if oracle(iv[:16 - 1 - j] + bytes([k]) + xor(iv[-j:], ans) + block):
                if iv[16 - 1 - j] != k: # prevent k set to original iv value
                    ans = bytes([iv[16 - 1 - j] ^ k ^ (0x80)]) + ans
                    print(ans)
                    f = 0
                    break
                else:
                    temp = bytes([iv[16 - 1 - j] ^ k ^ (0x80)])
        if f == 1:
            ans = temp + ans
    flag += ans
print(flag)