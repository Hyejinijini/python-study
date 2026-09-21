'''
집합 (set)
중복이 안되고, 순서가 없음
'''
# 3을 여러 개 적었음에도 불구하고 중복을 허용하지 않기 때문에 중복된 값은 무시되고 하나만 출력됨
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python에 모두 포함된 사람)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 또는 python에 포함된 사람)
# 순서가 없기 때문에 집합에 들어있기만 하면 순서없이 그냥 출력됨
print(java | python) # {'양세형', '박명수', '김태호', '유재석'}
print(java.union(python)) # {'양세형', '박명수', '김태호', '유재석'}

# 차집합 (java에는 있지만 python에는 존재하지 않는 사람)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# 집합에 값 추가하기
python.add("김태호")
print(python) # {'김태호', '유재석', '박명수'}

# 집합에 값 삭제하기
java.remove("김태호")
print(java) # {'유재석', '양세형'}