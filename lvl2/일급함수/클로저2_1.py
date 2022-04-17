# ?΄λ‘μ Έ ??­? ?? λ³??? ?΄κ°? ?¬?©?? €? ?¨? λ°κΉ₯?? μ§?? ? λ³??.


def closure_ex1():
    # ?? λ³??
    # ?΄λ‘μ?? ??­
    # ?΄ ??­? λ³??? ??΄?¬?΄ ????₯?΄??€.
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
print(average_function.__closure__)  # λ¦¬μ€?Έ ?€λΈμ ?Έ
print(average_function.__closure__[0].cell_contents)
