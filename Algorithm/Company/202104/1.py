def solution(s: str) -> str:
    """
    문자열 + ? => 팰린드롬 체크
    :param s: ?를 포함한 팰린드롬 문자열 -> [1, 1000]
    :return: 팰린드롬인 경우, 팰린드롬 문자열 'aaa', 만약 팰린드롬이 아닌 경우 'NO'
    """
    # 중앙값 및 팰린드롬 체크용 문자열 생성
    center_idx = len(s)//2

    # 가운데 string이 ?가 되는 경우 미리 체크
    if len(s) % 2 == 1 and s[center_idx] == '?':
        target = s[:center_idx] + 's' + s[center_idx+1:]
    else:
        target = s

    pre_list = target[:center_idx]
    post_list = target[center_idx:][::-1]

    pre_list = list(pre_list)
    post_list = list(post_list)

    # 팰린드롬 체크 및 생성 루프
    for idx in range(len(pre_list)):
        pre_c = pre_list[idx]
        post_c = post_list[idx]

        if pre_c != '?' and post_c != '?' and pre_c != post_c:
            return 'NO'
        elif pre_c != '?' and post_c == '?':
            post_list[idx] = pre_c
        elif pre_c == '?' and post_c != '?':
            pre_list[idx] = post_c
        elif pre_c == '?' and post_c == '?':
            pre_list[idx] = 'n'
            post_list[idx] = 'n'

    result = pre_list + post_list[::-1]
    return ''.join(item for item in result)


print(solution('bab??ad'))
print(solution('ab?ab'))
print(solution('?ab??a'))
print(solution('?a?'))
print(solution('?ab?bba?'))
print(solution('???'))
print(solution('?????'))
print(solution('??????'))
