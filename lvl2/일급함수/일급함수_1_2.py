def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


# 함수를 인수로 전달 및 함수로 결과 반환 -> 고위 함수
# map, filter, reduce

##지능형 리스트
print([factorial(i) for i in range(1, 6) if i % 2])
## 지능형 리스트처럼 일급함수를 이용
print(list(map(factorial, filter(lambda x: x % 2, range(1, 6)))))

##reduce 일급함수는 functools에서 임포트한다.
from functools import reduce
from operator import add

### 1부터 10까지 더하기
print(sum(range(1, 11)))
### reduce함수는 함수를 인자로 받아야한다.
print(reduce(add, range(1, 11)))

## 익명함수 lambda
print(reduce(lambda x, t: x + t, range(1, 11)))


# callable 함수 , 호출 연산자.
## 일급함수는 호출이 가능해야한다. 즉, 함수()를 실행하면 그 함수가 작동한다면, 일급함수; callable한 함수다.
print(callable(factorial))

# partial 함수. 함수를 인자로 받고 인자로 받은 함수의 인자를 고정시키는 역할
from operator import mul
from functools import partial

five = partial(mul, 5)
print(list(map(five, range(1, 10))))
