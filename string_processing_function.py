# 문자열 처리 함수

python = 'Python is Amazing'
print(python.lower()) # 모든 문자 소문자로 출력
print(python.upper()) # 모든 문자 대문자로 출력
print(python[0].isupper()) # 특정 위치에 있는 값이 대문자인지 판별, True
print(len(python)) # 문자열 길이 반환, 17
print(python.replace("Python", "Java")) # Python 문자를 찾아서 Java로 변경

index = python.index("n") # 문자열에서 'n'이라는 문자가 몇 번째 위치에 있는지 확인
print(index) # 5
index = python.index('n', index + 1) # 6번째 위치부터 계산하여 'n' 문자가 몇 번째 위치에 있는지 확인
print(index) # 15

print(python.find('Java')) # 내가 원하는 값이 없는 경우 -1을 반환, -1
# print(python.index('Java')) # error, 반환값없음

print(python.count('n')) # 특정 문자가 문자열에서 몇 번 등장하는지 확인, 2