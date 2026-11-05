# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#   print("이름: {0} 나이: {1}".format(name, age), end=" ")
#   print(lang1, lang2, lang3, lang4, lang5)

'''
end=" "의 역할:
해당 print문이 끝날 때, 줄바꿈 되지 않고 공백으로 끝낸다는 의미.
따라서 아래 print문이 하나의 줄로 출력됨.
'''
# profile("홍길동", 20, "Python", "Java", "C", "C++", "C#")
# # 이름: 홍길동 나이: 20 Python Java C C++ C#

# profile("맹구", 25, "Kotlin", "Swift", "", "", "")
# # 이름: 맹구 나이: 25 Kotlin Swift

'''
그런데 만약, 언어를 하나 더 추가하고 싶거나 언어를 5개까지 하지 못하는 사람의 프로필을 작성해야 한다면
1) 함수 자체를 lang6 을 추가해서 변경해야 되거나
2) 매번 빈 값을 넣어줘야 하는
번거로움이 생긴다.

이럴때 사용할 수 있는게 가변인자.
형식: *매개변수
'''
def profile(name, age, *language):
  print("이름: {0} 나이: {1}".format(name, age), end=" ")
  for lang in language:
    print(lang, end=" ")
  print()

profile("홍길동", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# 이름: 홍길동 나이: 20 Python Java C C++ C# JavaScript 

profile("맹구", 25, "Kotlin", "Swift")
# 이름: 맹구 나이: 25 Kotlin Swift