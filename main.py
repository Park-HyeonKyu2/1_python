import fruit # __name__ 값: fruit
#  if __name__ == "__main__": 블록은 실행되지 않음
from fruits import apple_info, banana_info, func1
# from fruits.apple import func1 # fruits 파일 안의 apple 파일 func1 함수를 부른다.
# from fruit import *

fruit.print_fruit("사과") # 파일이름.함수

result = fruit.add_quantity(10, 5) # quantity + amount
print(result)

apple = fruit.Fruit("사과", 10) # 클래스 객체 생성
apple.print_info()

print("*" * 30)
print(apple_info())
print(banana_info())
print(func1())