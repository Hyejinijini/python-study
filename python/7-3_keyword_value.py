# 키워드 값
def profile(name, age, main_lang):
  print(name, age, main_lang)

'''
키워드(매개변수)를 이용해서 함수를 호출해주면 순서가 뒤섞여 있어도 순서대로 출력됨.
'''
profile(name="홍길동", main_lang="파이썬", age=20) # 홍길동 20 파이썬
profile(main_lang="자바", age=25, name="짱구") # 짱구 25 자바