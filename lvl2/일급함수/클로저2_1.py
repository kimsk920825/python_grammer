# 클로져 영역의 자유변수는 내가 사용하려는 함수 바깥에서 지정된 변수.


def closure_ex1():
    # 자유변수
    # 클로저 영역
    # 이 영역의 변수는 파이썬이 저장해둔다.
    series = []

    def average(value):
        series.append(value)
        print(series, len(series))
        return sum(series) / len(series)

    return average


average_function = closure_ex1()
print(average_function(10))
print(average_function(20))
print(average_function(30))

print(dir(average_function))
print()
print("code>>>")
print(dir(average_function.__code__))
print()
print("co_freevars>>>")
print(average_function.__code__.co_freevars)
print()
print("co_cellvars>>>")
print(average_function.__code__.co_cellvars)
print()
print("__closure__>>>")
print(average_function.__closure__)  # 리스트 오브젝트
print(average_function.__closure__[0].cell_contents)

# 클로저 잘못된 방법
def closure_ex2():
    cnt = 0
    total = 0

    def average(value):
        cnt += 1
        total += value
        return total / cnt

    return average


average_function_2 = closure_ex2()

# print(average_function_2(10))
# UnboundLocalError: local variable 'cnt' referenced before assignment


def closure_ex3():
    cnt = 0
    total = 0

    def average(value):
        nonlocal cnt, total
        cnt += 1
        total += value
        return total / cnt

    return average


average_function_3 = closure_ex3()
print("nonlocal 예시", average_function_3(10))
