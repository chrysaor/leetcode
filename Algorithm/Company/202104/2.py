def solution(s):
    """
    코인 뒤집기
    :param s: 1과 0으로 이루어진 배역 [1, 0, 0, 1 ...]
    :return: 앞면과 뒷면으로 구성된 배열을 만들 수 있는 최소 뒤집기 횟수
    """
    print(s)
    # Step 1. 가장 큰 길이의 반복 패턴을 찾는다.
    start = 0
    last = 0

    max_val = 0
    max_list = (0, 0)

    prev_char = s[0]
    for idx, item in enumerate(s[1:]):
        if item != prev_char:
            last = idx + 1
            if last - start > max_val:
                max_val = last - start
                max_list = (start, last)
        else:
            if last - start > max_val:
                max_val = last - start
                max_list = (start, last)
            start = idx + 1

        # 직전 문자 교체
        prev_char = item

    result = 0
    print(max_list)
    # 만약 주어진 문자열이 이미 완성되어 있는 경우
    if max_list[1] - max_list[0] + 1 == len(s):
        return 0

    result_map = {0: 1, 1: 0}

    # 오른쪽 방향 탐색
    right_item = s[max_list[1]]
    for idx in range(max_list[1] + 1, len(s)):
        if right_item == s[idx]:
            s[idx] = result_map[right_item]
            result += 1

        right_item = s[idx]

    # 왼쪽 방향 탐색
    left_item = s[max_list[0]]
    for idx in range(max_list[0] - 1, 0, -1):
        if left_item == s[idx]:
            result += 1
            s[idx] = result_map[right_item]

        left_item = s[idx]

    return result


print(solution([1, 0, 1, 0, 1]))
print(solution([1, 0, 1, 0, 1, 1]))
print(solution([0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]))
print(solution([0, 1, 1, 0]))
print(solution([0, 1, 0]))
print(solution([1, 1, 1, 1]))
print(solution([1, 1, 1, 1, 1, 1]))
