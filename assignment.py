
# 치환문 예
a=1
b=a+1
print(a, b)

# 변수값 할당 오류
# 1 + a = c

e = 3.5; f = 5.3
print(e, f)

e ,f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 할당할 때
x = y = z = 10
print(x, y, z)

# 동적 타이핑: 변수에 새로운 값이 할당되면 기존의 값을 버리고
# 새로운 값(타입)으로 치환된다.

a = 1
print(a, type(a))
a ="hello"
print(a, type(a))

# 확장 치환문
a = 10
a += 10

print(a)



















