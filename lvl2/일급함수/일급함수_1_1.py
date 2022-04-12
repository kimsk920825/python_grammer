def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


# 일급 함수를 객체로 취급할 수 있을까?


# factorial 함수만 가진 특징
## print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

factorial_b = set(sorted(dir(factorial))) - set(sorted(dir(A)))
# factorial 함수 속성 중 클래스와 공통되는 부부분
factorial_a = set(sorted(dir(factorial))) - (
    set(sorted(dir(factorial))) - set(sorted(dir(A)))
)

## print(factorial_a)

# 함수와 클래스의 타입 검색
print(type(factorial))
print(type(A))
# 결론: factorial 함수의 속성을 확인해보면 클래스가 가진 속성을 포함한다는 것을 알 수 있다. 즉, 파이썬에서 함수는 객체취급을 한다.

# 일급 함수는 변수에 할당 할 수 있을까?
## 실행하지 않고 함수 자체를 할당
var_func = factorial

print(var_func)  # 함수가 어느 메모리 위치에 저장되있는지 출력
print(var_func(4))  # 함수 실행 값 출력
