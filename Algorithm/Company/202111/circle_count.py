import math


def check_circle(x1: int, y1: int, r1: float, x2: int, y2: int, r2: float) -> bool:
    """
    두 원의 위치관계 -> 두 원이 내접 혹은 내부에 있어 만나지 않으면 True 반환
    Args:
        x1: x값
        y1: y값
        r1: 반지름
        x2: x값
        y2: y값
        r2: 반지름

    Returns:
        bool: 내접하거나 내부에 있는 경우는 True
    """
    r_minus = abs(r1 - r2)
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return True if r_minus >= dist else False


print(check_circle(1, 1, 1, 3, 3, 10))
print(check_circle(1, 1, 2, 3, 3, 2))
