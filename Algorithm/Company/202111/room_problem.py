def get_clean_room(size: int, is_horizontal: bool):
    """
    N*N 사이즈의 크기의 방을 만들고, 로봇 청소기를 이용하여 청소를 시작한다.
    각 행과 열은 max(행, 열) 값을 경계로 설정하여 넘어가지 않는다.
    1 -> 3 -> 5 -> ...

    예) n = 3, horizontal = True, 시작점 0, 0
    0 0 0    1 2 9
    0 0 0 => 4 3 8
    0 0 0    5 6 7

    :param size: 방 사이즈 (n * n 사이즈)
    :param is_horizontal: 최초 동작시 수평 여부
    :return: array[n][n] - 청소가 끝난 배열
    """
    def check(c_x, c_y, c_n):
        if 0 <= c_x <= c_n - 1 and 0 <= c_y <= c_n - 1:
            return True if room[c_x][c_y] == 0 else False
        else:
            return False

    if size == 1:
        return [[1]]

    n = size
    horizontal = is_horizontal

    room = []
    for idx in range(n):
        room.append([0] * n)

    x, y = 0, 0
    h_move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    v_move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    count = 0

    for idx in range(1, n):
        # 방향 설정
        m = h_move if horizontal else v_move
        c_idx = idx + 1

        while count < c_idx ** 2:
            if check(x, y, c_idx):
                count += 1
                room[x][y] = count

            if check(x+m[0][0], y+m[0][1], c_idx):
                x += m[0][0]
                y += m[0][1]
            elif check(x + m[1][0], y + m[1][1], c_idx):
                x += m[1][0]
                y += m[1][1]
            elif check(x + m[2][0], y + m[2][1], c_idx):
                x += m[2][0]
                y += m[2][1]
            elif check(x + m[3][0], y + m[3][1], c_idx):
                x += m[3][0]
                y += m[3][1]

        horizontal = not horizontal
        if horizontal:
            y += 1
        else:
            x += 1

    return room


target = get_room(10, True)
for idx in range(len(target)):
    print(target[idx])
