# ?��로져 ?��?��?�� ?��?���??��?�� ?���? ?��?��?��?��?�� ?��?�� 바깥?��?�� �??��?�� �??��.


def closure_ex1():
    # ?��?���??��
    # ?��로�?? ?��?��
    # ?�� ?��?��?�� �??��?�� ?��?��?��?�� ????��?��?��?��.
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
print(average_function.__closure__)  # 리스?�� ?��브젝?��
print(average_function.__closure__[0].cell_contents)
