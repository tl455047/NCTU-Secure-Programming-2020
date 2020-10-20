#!/usr/bin/env python3
from functools import reduce

class LFSR:
    def __init__(self, init, feedback):
        self.state = init
        self.feedback = feedback
    def getbit(self):
        nextbit = reduce(lambda x, y: x ^ y, [i & j for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit

class MYLFSR:
    def __init__(self, inits):
        inits = [[int(i) for i in f"{int.from_bytes(init, 'big'):016b}"] for init in inits]
        self.l1 = LFSR(inits[0], [int(i) for i in f'{39989:016b}'])
        self.l2 = LFSR(inits[1], [int(i) for i in f'{40111:016b}'])
        self.l3 = LFSR(inits[2], [int(i) for i in f'{52453:016b}'])

    def getbit(self):
        x1 = self.l1.getbit()
        x2 = self.l2.getbit()
        x3 = self.l3.getbit() 
        return (x1 & x2) ^ ((not x1) & x3)

    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])
'''
f = open('./output.txt', 'r')
output = []
while 1:
    c = f.read(1)
    if not c:
        break
    elif c == '1' or c == '0':
        output.append(int(c))
'''    
output = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
print(output)
# find the highest correlation between x3 and output
init_X3 = 0
correlate = 0.0
FLAG = b'000000'
for i in range(pow(2,16)):
    lfsr =  LFSR([int(i) for i in f"{int.from_bytes(i.to_bytes(2, 'big'), 'big'):016b}"], [int(i) for i in f'{52453:016b}'])
    count = 0
    for j in range(100):
        x3 = lfsr.getbit()
        if x3 == output[j]:
            count += 1
    rate = count/100
    if rate > 0.7 and correlate < rate:
            correlate = rate
            init_X3 = i
print(str(init_X3) + ' '+ str(correlate))
# find the highest correlation between x2 and output
init_X2 = 0
correlate = 0.0
FLAG = b'000000'
for i in range(pow(2,16)):
    lfsr =  LFSR([int(i) for i in f"{int.from_bytes(i.to_bytes(2, 'big'), 'big'):016b}"], [int(i) for i in f'{40111:016b}'])
    count = 0
    for j in range(100):
        x2 = lfsr.getbit()
        if x2 == output[j]:
            count += 1
    rate = count/100
    if rate > 0.7 and correlate < rate:
            correlate = rate
            init_X2 = i
print(str(init_X2) + ' '+ str(correlate))
# use the x2, x3 we find to find x1
for i in range(pow(2,16)):
    lfsr = MYLFSR([i.to_bytes(2, 'big'), init_X2.to_bytes(2, 'big'), init_X3.to_bytes(2, 'big')])
    lis = [lfsr.getbit() for _ in range(100)]
    if output == lis:
        print("FLAG[0:2]: " + str(i.to_bytes(2, 'big')))
        print("FLAG[2:4]: " + str(init_X2.to_bytes(2, 'big')))
        print("FLAG[4:6]: " + str(init_X3.to_bytes(2, 'big')))
        flag = b"FLAG{" + i.to_bytes(2, 'big') + init_X2.to_bytes(2, 'big') + init_X3.to_bytes(2, 'big') + b"}"
        print(flag)
        break