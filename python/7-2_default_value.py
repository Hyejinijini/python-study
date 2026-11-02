# 함수 기본값

def profile(name, age, main_lang):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("홍길동", 20, "파이썬")

# 만약, 같은 학교 / 같은 학년 / 같은 반 / 같은 수업을 듣는다고 가정하자.
def profile(name, age = 17, main_lang = "파이썬"):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("홍길동") # 이름: 홍길동   나이: 17   주 사용 언어: 파이썬