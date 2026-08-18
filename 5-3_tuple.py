# 튜플
'''
튜플은 리스트(list)와 다르게 내용 변경 및 추가가 불가능하지만,
속도가 리스트보다 빠르다.
따라서, 변경되지 않는 목록을 사용할 때 활용함.
'''
# 절대 메뉴 변경 없이 돈까스와 치즈까스만 제공한다고 가정.
menu = ("돈까스", "치즈까스")

print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# 새로운 값을 추가하려고 하면? Error 발생.
# menu.add("생선까스") # Error

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "hobby")
print(name, age, hobby) # 김종국 20 코딩
