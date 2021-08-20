# Code for Breadth first search for liquid sorting game
import copy
import queue
import time
import pdb


answer = []

sequence_queue = queue.Queue()

# bottom to top means leftmost element to rightmost element in array
state0 = {
    1: ["grey", "brown", "orange", "lblue"],
    2: ["purple", "lgreen", "yellow", "grey"],
    3: ["lblue", "pink", "green", "orange"],
    4: ["yellow", "red", "yellow", "blue"],
    5: ["yellow", "orange", "purple", "brown"],
    6: ["dgreen", "green", "lgreen", "dgreen"],
    7: ["blue", "red", "blue", "green"],
    8: ["red", "brown", "lgreen", "brown"],
    9: ["purple", "lblue", "lgreen", "pink"],
    10: ["pink", "orange", "green", "purple"],
    11: ["dgreen", "dgreen", "pink", "grey"],
    12: ["blue", "lblue", "red", "grey"],
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


stateX = state0

for i in range(1, 1 + len(state0)):
    for j in range(1, 1 + len(state0)):
        if i != j:
            stateX = copy.deepcopy(state0)
            val = pour(stateX[i], stateX[j])
            sequence_list = [(i, j)]
            if val:
                sequence_queue.put(sequence_list)

flag = True
while flag:
    temp_queue = queue.Queue()
    while not sequence_queue.empty():
        stateX = copy.deepcopy(state0)
        seq_n = sequence_queue.get()

        # stateX has reached the sequence end of latest level
        for seq in seq_n:
            pour(stateX[seq[0]], stateX[seq[1]])

        # Check if sequence is final
        if check_final_state(stateX):
            print("\n\nFinal Sequence:-\n\n")
            print(seq_n)
            flag = False
            break

        # Now apply the rule
        for i in range(1, 1 + len(stateX)):
            for j in range(1, 1 + len(stateX)):
                if i != j:
                    stateY = copy.deepcopy(stateX)
                    val = pour(stateY[i], stateY[j])
                    seq_n_copy = copy.deepcopy(seq_n)
                    seq_n_copy.append((i, j))
                    if val:
                        temp_queue.put(seq_n_copy)
    sequence_queue = temp_queue


print("\n\nFinal State:-\n\n")
print(stateX)
# print("\n\nSequence Queue:-\n\n")
# print(sequence_queue.queue)
