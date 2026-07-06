# 연산자

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 제곱 값, 8
print(5%3) # 나머지 값, 2
print(10%3) # 1
print(5//3) # 몫 값, 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # 같은 값인지 비교, True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # 같지 않음, True
print(not(1 != 3)) # 반대 값, False

print((3 > 0) and (3 < 5)) # 모두 True안 경우에만 True, True
print((3 > 0) & (3 < 5)) # & = and, True

print((3 > 0) or (3 > 5)) # 하나만 True여도 True, True
print((3 > 0) | (3 > 5)) # | = or, True

print(5 > 4 > 3) # Ture
print(5 > 4 > 7) # False