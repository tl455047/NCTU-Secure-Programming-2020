#!/usr/bin/python3
import time as 時間
import random as 隨機
from typing import List as 陣列
from io import BufferedReader as 緩衝讀取者
from forbiddenfruit import curse as 詛咒

整數 = int
詛咒(整數, "從位元組", 整數.from_bytes)
詛咒(整數, "到位元組", 整數.to_bytes)
位元組 = bytes
詛咒(位元組, "十六進制", 位元組.hex)
詛咒(位元組, "加入", 位元組.join)
詛咒(緩衝讀取者, "讀取", 緩衝讀取者.read)
隨機.種子 = 隨機.seed
隨機.給我隨機位元們 = 隨機.getrandbits
時間.現在 = 時間.time
列印 = print
打開 = open
範圍 = range
長度 = len
大端序 = 'big'
讀取位元組 = 'rb'
import os
def 正轉換(資料, 大小=4):
    return [整數.從位元組(資料[索引:索引+大小], 大端序) for 索引 in 範圍(0, 長度(資料), 大小)]

def 逆轉換(資料, 大小=4):
    return b''.加入([元素.到位元組(大小, 大端序) for 元素 in 資料])

def _加密(向量: 陣列[整數], 金鑰: 陣列[整數]):
    累加, 得優塔, 遮罩 = 0, 0xFACEB00C, 0xffffffff
    for 次數 in 範圍(32):

        累加 = 累加 + 得優塔 & 遮罩
    
        向量[0] = 向量[0] + ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累加) & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        向量[1] = 向量[1] + ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累加) & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
    return 向量

def 加密(明文: 位元組, 密鑰: 位元組):
    密文 = b''
    for 索引 in 範圍(0, 長度(明文), 8):
        密文 += 逆轉換(_加密(正轉換(明文[索引:索引+8]), 正轉換(密鑰)))
    return 密文
def decrypt(cipher: 位元組, 金鑰: 位元組):
    plain = b''
    for 索引 in 範圍(0, 長度(cipher), 8):
        plain += 逆轉換(_decrypt(正轉換(cipher[索引:索引+8]), 正轉換(金鑰)))
    return plain
def _decrypt(向量: 陣列[整數], 金鑰: 陣列[整數]):
    累加, 得優塔, 遮罩 = 0, 0xFACEB00C, 0xffffffff
    for 次數 in 範圍(32):
        累加 = 累加 + 得優塔 & 遮罩
    for 次數 in 範圍(32):
        向量[1] = 向量[1] - ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累加) & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
        向量[0] = 向量[0] - ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累加) & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        累加 = 累加 - 得優塔 & 遮罩
        
    return 向量    
if __name__ == '__main__':
    #cipher = 打開('旗幟', 讀取位元組).讀取()
    #assert 長度(旗幟) == 16

    #check decrypt function
    #c = 加密(b'1111111111111111',密鑰)
    #plain = decrypt(c, 密鑰)
    #列印('明文 = ' + str(plain))
    
    i = 1600390800-1  # 2020/9/18/09:00
    cipher = bytes.fromhex('77f905c39e36b5eb0deecbb4eb08e8cb')
    assert 長度(cipher) == 16
    while i < 1600390800:
        隨機.種子(整數(i))
        密鑰 = 隨機.給我隨機位元們(128).到位元組(16, 大端序)
          
        plain = decrypt(cipher, 密鑰)
        
        print("seed: " + str(i))
        
        if b'flag' in plain:
          列印('明文 = ' + str(plain))
          break
        elif b'FLAG' in plain:
          列印('明文 = ' + str(plain))
          break
        i -= 1
    
