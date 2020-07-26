import copy
import itertools


def get_groups(size):
    """ starting from the board size, find all groups of decision variables v_i """
    groups = {}
    for i in range(1, size ** 2 + 1):
        neig_i = []
        neig_i.append(i)
        if not i % size == 1:
            neig_i.append(i - 1)
        if not i % size == 0:
            neig_i.append(i + 1)
        if i - size > 0:
            neig_i.append(i - size)
        if i + size <= size ** 2:
            neig_i.append(i + size)
        groups[i] = neig_i
    return groups


def get_next_group(groups, values, board):
    """ get the next equation to solve """
    unk = []
    for group in groups.items():
        group_values = [values[i - 1] for i in group[1]]
        unk.append(len([i for i, x in enumerate(group_values) if x == -1]))
    M = max(unk)
    if M == 0:
        return validate(groups, values, board)
    for it, u in enumerate(unk):
        if u == 0:
            unk[it] = M + 1
    next_group = unk.index(min(unk)) + 1
    return next_group


def get_combinations(values, board, groups):
    """ recursively compute the combinations that satisfy the game equations """
    next_group = get_next_group(groups, values, board)
    if next_group == -1:
        return True
    if next_group == -2:
        return False
    # print(next_group)
    # compute sum of known variables in group
    sum = 0
    remaining = copy.copy(groups[next_group])
    for it in groups[next_group]:
        if values[it - 1] > -1:
            sum += values[it - 1]
            remaining.remove(it)
    if board[next_group - 1] == 0:  # odd combinations
        if sum % 2 == 1:
            r = range(0, len(remaining) + 1, 2)
        else:
            r = range(1, len(remaining) + 1, 2)
    else:  # even combinations
        if sum % 2 == 1:
            r = range(1, len(remaining) + 1, 2)
        else:
            r = range(0, len(remaining) + 1, 2)
    for i in r:
        v_it = [0] * len(remaining)
        for j in range(i):
            v_it[j] = 1
        for k in set(itertools.permutations(v_it)):
            for idx, m in enumerate(k):
                values[remaining[idx] - 1] = m
            # recursion here
            status = get_combinations(values, board, groups)
            if status:
                return True
            else:
                for idx, m in enumerate(k):
                    values[remaining[idx] - 1] = -1


def validate(groups, values, board):
    for g in groups:
        group_values = [values[i - 1] for i in groups[g]]
        if board[g - 1] == 0 and sum(group_values) % 2 == 0:
            return -2  # error
        if board[g - 1] == 1 and sum(group_values) % 2 == 1:
            return -2  # error
    return -1


if __name__ == "__main__":
    size = 2
    # board = [1, 0, 0, 0, 0, 1, 1, 0, 1]
    board = [1, 1, 1, 0]
    values = [-1] * size ** 2
    groups = get_groups(size)
    print(groups)
    get_combinations(values, board, groups)
    print(values)
