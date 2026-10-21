# 사전 자료형
'''
{key:value} 형태

key와 value를 한 쌍으로 가지는 자료형으로,
key에 대한 중복이 허용되지 않는다.
'''

cabinet = {3:"유재석", 100:"김태호"} # key1: 3, value1: 유재석 / key2: 100, value2: 김태호

# 사전 자료형에서 값을 가져오는 방법 1. 대괄호 사용
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

# 2. .get() 사용
print(cabinet.get(3)) # 유재석

# 존재하지 않는 key값 출력 1
'''
5라는 key값은 없기 때문에 해당 부분에서 Error 발생
따라서 "hi"문자는 출력되지 않음
'''
# print(cabinet[5])
# print("hi")

# 존재하지 않는 key값 출력 2
'''
.get()을 사용하면 key값이 없을 경우 None을 반환하여 Error가 발생하지 않고,
정상적으로 다음 코드가 실행됨
'''
print(cabinet.get(5)) # None
print("hi") # hi

# 존재하지 않는 key값 출력 3
'''
5번 key가 없으면 대신 보여줄 문자열 지정 가능
'''
print(cabinet.get(5)) # None
print(cabinet.get(5, '사용 가능')) # 사용 가능

# 어떤 값이 있는지 확인하는 방법
'''
형태: key in 변수

변수에 key값이 존재하면 True,
key값이 존재하지 않으면 False를 출력
'''
print(3 in cabinet) # True
print(5 in cabinet) # False


# - - - - - - - - - - -


# String 자료형
cabinet = {"A-3":"유재석", "B-100":"김태호"}

print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새로운 key 추가
'''
만약, "c-20"이라는 key가 이미 존재하는 경우에는
기존 값이 업데이트 됨
'''
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"

print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'c-20': '조세호'}

# key 삭제
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'c-20': '조세호'}

# key 만 출력하는 방법
print(cabinet.keys()) # dict_keys(['B-100', 'c-20'])

# value 만 출력하는 방법
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력하는 방법
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('c-20', '조세호')])

# 모든 값 삭제
print(cabinet.clear()) # None