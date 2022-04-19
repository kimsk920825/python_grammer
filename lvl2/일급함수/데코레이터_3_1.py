# 일급함수정리
# 인자로 함수를 넘길 수 있고, 함수를 결과값으로 반환할 수 있으며, 변수로 함수를 지정할 수 있다.

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅,프레임워크, 유효성 체크 -> 공통 기능 적용 가능
# 3. 조합해서 사용 용이
# 단점
# 1. 가독성이 떨어질 수 있다.
# 2. 특정 기능에 한정된 함수는 ->단일 함수로 작성하는 것이 유리


import time
from unittest import result


def perf_clock(func):
    # 자유변수 영역
    # 만약 자유변수에 아무런 변수가 없다면 매개변수로 넘어온 함수에 상태와 레퍼렌스를 계속 저장하고 사용한다. 아우터 func에서 넘어온 인자를 내부에서 가져온다.
    def per_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ",".join(repr(arg) for arg in args)
        # 결과 출력
        print("[%0.5fs] %s(%s) -> %r" % (et, name, arg_str, result))
        return result

    return per_clocked
