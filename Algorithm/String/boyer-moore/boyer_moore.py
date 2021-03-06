

def boyer_moore_search(source: str, target: str) -> int:
    """
    보이어 무어 알고리즘을 통해 source 문자열에서 target을 검색한다.
    :param source: Source 문자열
    :param target: 찾고자 하는 문자열
    :return: 만약 해당 문자열이 source에 있다면 최초 위치 인덱스, 없다면 -1
    """
    # String table -> 검색 문자열 리스트
    string_table = list(target)
    # Skip table -> 문자 일치 여부에 따른 이동 거리
    skip_table = [idx for idx in range(len(target) - 1, -1, -1)] + [len(target)]
    # String set -> 본문의 문자가 검색 문자열에 있는지 확인을 위한 set
    string_set = set(string_table)

    print(string_table, skip_table, string_set)

    # 시작 인덱스
    cur_idx = skip_table[-1]

    while cur_idx < len(source):
        if source[cur_idx] == target[-1]:
            # 끝 문자가 매칭 되는 경우
            source_idx = cur_idx - 1
            for s_idx in range(len(target) - 1, -1, -1):
                if target[s_idx] != source[source_idx]:
                    cur_idx += skip_table[s_idx]
                    break
                source_idx -= 1
            return cur_idx - len(target) + 1
        elif source[cur_idx] != target[-1] and source[cur_idx] in string_set:
            # 끝 문자가 다르고 해당 문자가 존재 하는 경우
            for f_idx in range(len(target)):
                if target[f_idx] == source[cur_idx]:
                    cur_idx -= f_idx + 1
                    break
        else:
            # 끝 문자가 다르고 해당 문자가 존재 하는 경우
            cur_idx += skip_table[-1]

    return -1


assert boyer_moore_search('My Hat is Super hat', 'is') == 'My Hat is Super hat'.index('is')
assert boyer_moore_search('My Hat is Super hat', 'Hat') == 'My Hat is Super hat'.index('Hat')
assert boyer_moore_search('이메일 문자 수신을 동의하려면 말이지요.. 그거 아십니까?', '그거') == 24
assert boyer_moore_search('이메일 문자 수신을 동의하려면 말이지요.. 그거 아십니까?', '하려면') == 13
assert boyer_moore_search('이메일 문자 수신을 동의하려면 말이지요.. 그거 아십니까?', '?') == 31
