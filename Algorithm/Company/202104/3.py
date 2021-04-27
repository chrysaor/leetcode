def solution(n: int) -> int:
    """Integer n -> Insert '5' digits to integer -> Maximum integer value

    :param n: int value in the range [-8000 ~ 8000]
    :return: int
    """
    # 0인 경우 최대값 50
    if n == 0:
        return 50

    # 검색할 문자열 설정
    target = str(n)

    # TODO: 조금 더 적은 라인으로 최적화 가능?
    if n < 0:
        # 0 보다 작은 경우
        result = '-'

        # 반복하며 5의 위치를 탐색
        for idx, item in enumerate(target[1:]):
            if int(item) > 5:
                result += '5' + target[idx+1:]
                break
            else:
                result += item
    else:
        # 0보다 큰 경우
        result = ''

        # 반복하며 5의 위치를 탐색
        for idx, item in enumerate(target):
            if int(item) <= 5:
                result += '5' + target[idx:]
                break
            else:
                result += item

    # 발견하지 못한 경우 처리
    if len(result) == len(target):
        result += '5'

    return int(result)


print(solution(-501))
print(solution(268))
print(solution(670))
print(solution(0))
print(solution(-161))
print(solution(-999))
