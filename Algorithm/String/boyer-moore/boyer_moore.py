

class BoyerMooreSearch:
    def __init__(self, target):
        string_table = list(target)
        move_count = [idx for idx in range(len(target)+1, -1, -1)]
        string_set = set(string_table)
