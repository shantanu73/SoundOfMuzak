# Code for Depth first search for liquid sorting game
import copy
import queue
import time
import pdb


answer = []

# bottom to top means leftmost element to rightmost element in array
state0 = {
    1: ["lgreen", "brown", "green", "brown"],
    2: ["green", "lblue", "grey", "lgreen"],
    3: ["yellow", "lgreen", "green", "red"],
    4: ["purple", "yellow", "red", "pink"],
    5: ["green", "red", "pink", "lgreen"],
    6: ["grey", "pink", "blue", "grey"],
    7: ["dgreen", "yellow", "blue", "orange"],
    8: ["dgreen", "orange", "orange", "purple"],
    9: ["red", "orange", "blue", "lblue"],
    10: ["lblue", "dgreen", "dgreen", "purple"],
    11: ["blue", "purple", "pink", "yellow"],
    12: ["grey", "brown", "brown", "lblue"],
    13: [],
    14: [],
}

# state0 = {
#     1: ["grey", "brown", "orange", "lblue"],
#     2: ["purple", "lgreen", "yellow", "grey"],
#     3: ["lblue", "pink", "green", "orange"],
#     4: ["yellow", "red", "yellow", "blue"],
#     5: ["yellow", "orange", "purple", "brown"],
#     6: ["dgreen", "green", "lgreen", "dgreen"],
#     7: ["blue", "red", "blue", "green"],
#     8: ["red", "brown", "lgreen", "brown"],
#     9: ["purple", "lblue", "lgreen", "pink"],
#     10: ["pink", "orange", "green", "purple"],
#     11: ["dgreen", "dgreen", "pink", "grey"],
#     12: ["blue", "lblue", "red", "grey"],
#     13: [],
#     14: [],
# }

# state0 = {
#     1: ["grey", "brown", "orange", "lblue"],
#     2: ["purple", "lgreen", "yellow", "grey"],
#     3: ["lblue", "pink", "green", "orange"],
#     4: ["yellow", "red", "yellow", "blue"],
#     5: ["yellow", "orange", "purple", "brown"],
#     6: ["dgreen", "green", "lgreen", "dgreen"],
#     7: ["blue", "red", "blue", "green"],
#     8: ["red", "brown", "lgreen", "brown"],
#     9: ["purple", "lblue", "lgreen", "pink"],
#     10: ["pink", "orange", "green", "purple"],
#     11: ["dgreen", "dgreen", "pink", "grey"],
#     12: ["blue", "lblue", "red", "grey"],
#     13: [],
#     14: [],
# }


# state0 = {
#     1: ["grey", "grey", "grey", "blue"],
#     2: ["blue", "blue", "yellow", "grey"],
#     3: ["yellow", "yellow", "blue", "yellow"],
#     4: [],
#     5: [],
# }


def check_final_state(state={}):
    """
    Checks if the final state is reached.
    :param state: dict
    :return: bool
    """

    for tube_content in state.values():
        if len(tube_content) == 4:
            for color in tube_content:
                if color != tube_content[0]:
                    return False
        elif len(tube_content) != 0:
            return False

    return True


def pour(glass1=[], glass2=[]):
    """
    Pour from glass1 to glass2

    :param glass1: list
    :param glass2: list
    :return: bool
    """

    # empty glass1 or full glass2
    if len(glass1) == 0 or len(glass2) == 4:
        return False

    g1_top = glass1.pop()
    glass1.append(g1_top)

    # not empty glass2
    if len(glass2) != 0:
        g2_top = glass2.pop()
        glass2.append(g2_top)

        if g1_top != g2_top:
            return False

        pour_done = False
        while len(glass1) > 0 and len(glass2) < 4 and not pour_done:
            g1_top = glass1.pop()
            g2_top = glass2.pop()
            if g1_top != g2_top:
                pour_done = True
                glass1.append(g1_top)
                glass2.append(g2_top)
            else:
                glass2.append(g1_top)
                glass2.append(g2_top)
    else:
        # empty glass2
        pour_done = False
        while len(glass1) > 0 and not pour_done:
            temp = glass1.pop()
            if g1_top == temp:
                glass2.append(temp)
            else:
                pour_done = True
                glass1.append(temp)

        if len(glass1) == 0:
            return False

    return True


def dfs_func(state):

    print(state)

    # pdb.set_trace()

    if check_final_state(state):
        print("\n\nFinal Sequence:-\n\n")
        print(answer)
        print("\n\nFinal State:-\n\n")
        print(state)
        return True

    for i in range(1, 1 + len(state)):
        for j in range(1, 1 + len(state)):
            if i != j:
                state_temp = copy.deepcopy(state)
                val = pour(state_temp[i], state_temp[j])
                if val:
                    if len(answer) < 2 or (len(answer) > 1 and answer[len(answer)-2] != (i, j)):
                        answer.append((i, j))
                        if dfs_func(state_temp):
                            return True

    if len(answer) > 0:
        answer.pop()
    return False


print("\n\nDFS output:-\n\n")
print(dfs_func(state0))


# print("\n\nFinal State:-\n\n")
# print(state0)
# print(stateX)
# print("\n\nSequence Queue:-\n\n")
# print(sequence_queue.queue)
