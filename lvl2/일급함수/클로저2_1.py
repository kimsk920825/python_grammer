# ?´ë¡œì ¸ ?˜?—­?˜ ??œ ë³??ˆ˜?Š” ?‚´ê°? ?‚¬?š©?•˜? ¤?Š” ?•¨?ˆ˜ ë°”ê¹¥?—?„œ ì§?? •?œ ë³??ˆ˜.


def closure_ex1():
    # ??œ ë³??ˆ˜
    # ?´ë¡œì?? ?˜?—­
    # ?´ ?˜?—­?˜ ë³??ˆ˜?Š” ?ŒŒ?´?¬?´ ????¥?•´?‘”?‹¤.
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
print(average_function.__closure__)  # ë¦¬ìŠ¤?Š¸ ?˜¤ë¸Œì ?Š¸
print(average_function.__closure__[0].cell_contents)
