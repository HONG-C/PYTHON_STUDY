"""파이썬 공부 1일차"""

#1.기본 연산
a=3        #자료형 선언 불필요!
b=1.5
print("a+b:")
print(a+b) #서식문자 불필요!파이썬은 주석을 //이 아니라 #으로 표시함!
print("a/b:")
print(a/b)
print("a*b:")
print(a*b)
c="python"
print(c)
a=2+3j    #복소수도 연산 가능!
b=3
print(a*b)
print("\n\n")


#2 조건문
if b>1:
  print("b는 1보다 크네!")

#3 반복문
for a in [1,2,3]:
  print(a)

i=0
while i<3:
  i=i+1
  print(i)

#4 함수
def sum(a,b):
  return a+b
print(sum(3,4))  