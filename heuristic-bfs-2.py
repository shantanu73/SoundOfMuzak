# Code for Heuristic Best first search for liquid sorting game
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

# state0 = {
#     1: ["c1", "c2", "c3", "c2"],
#     2: ["c4", "c4", "c3", "c2"],
#     3: ["c5", "c5", "c4", "c2"],
#     4: ["c1", "c5", "c3", "c4"],
#     5: ["c1", "c3", "c1", "c5"],
#     6: [],
#     7: [],
# }

state0 = {
    1: ["o", "dblu", "g", "pi"],
    2: ["gra", "o", "pur", "r"],
    3: ["r", "lg", "gra", "lg"],
    4: ["dblu", "dblu", "lg", "pi"],
    5: ["o", "g", "r", "blu"],
    6: ["g", "blu", "gra", "blu"],
    7: ["gra", "pur", "r", "pur"],
    8: ["blu", "pi", "dblu", "lg"],
    9: ["pi", "g", "o", "pur"],
    10: [],
    11: [],
}


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


def distinct(tube):
    # Put all array elements in a map
    distinct_colors = set()
    for color in tube:
        distinct_colors.add(color)

    return len(distinct_colors)


def tube_cost(tube=[]):
    tube_length = len(tube)

    if tube_length < 2:
        return tube_length
    distinct_colors = distinct(tube)
    if distinct_colors == tube_length:
        # all distinct colors
        return 2*tube_length - 1

    if distinct_colors == 1:
        # all same color
        if tube_length == 4:
            return 0
        return 1
    if tube_length == 3:
        if tube[0] == tube[1]:
            return tube_length
        return tube_length - 1
    else:
        # length of tube is 4
        if tube[0] == tube[1]:
            return tube_length + 2
        elif tube[1] == tube[2]:
            return tube_length + 1
        elif tube[2] == tube[3]:
            return tube_length
        elif tube[0] == tube[1] and tube[1] == tube[2]:
            return tube_length - 1

        # Basically when tube[3] == tube[2] and tube[1] == tube[2]:
        return tube_length - 2


def state_cost(state={}):
    total_cost = 0
    for tube in state.values():
        total_cost = total_cost + tube_cost(tube)

    return total_cost


state0_cost = state_cost(state0)

stateX_cost = state0_cost
stateX = state0

for i in range(1, 1 + len(state0)):
    for j in range(1, 1 + len(state0)):
        if i != j:
            stateX_cost = copy.deepcopy(state0_cost)
            stateX = copy.deepcopy(state0)
            cost_i = tube_cost(stateX[i])
            cost_j = tube_cost(stateX[j])
            val = pour(stateX[i], stateX[j])
            if val:
                sequence_list = [(i, j)]
                modified_cost_i = tube_cost(stateX[i])
                modified_cost_j = tube_cost(stateX[j])
                cost = stateX_cost - cost_i - cost_j + modified_cost_i + modified_cost_j
                sequence_queue.put({
                    "cost": cost,
                    "list": sequence_list
                })

while True:
    # print("\nApna Queue\n")
    # print(sequence_queue.queue)
    # time.sleep(5)
    stateX = copy.deepcopy(state0)

    # pull out the min cost sequence

    min_index = 0
    for i in range(sequence_queue.qsize()):
        if sequence_queue.queue[i]["cost"] < sequence_queue.queue[min_index]["cost"]:
            min_index = i
    seq_n = sequence_queue.queue[min_index]
    del sequence_queue.queue[min_index]

    # stateX has reached the sequence end of latest level
    for seq in seq_n["list"]:
        pour(stateX[seq[0]], stateX[seq[1]])

    # Check if sequence is final
    if check_final_state(stateX):
        print("\n\nFinal Sequence:-\n\n")
        print(seq_n["list"])
        print("\n\nFinal Cost:-\n\n")
        print(seq_n["cost"])
        break

    # Now apply the rule
    for i in range(1, 1 + len(stateX)):
        for j in range(1, 1 + len(stateX)):
            if i != j:
                stateY = copy.deepcopy(stateX)
                stateY_cost = copy.deepcopy(seq_n["cost"])
                cost_i = tube_cost(stateY[i])
                cost_j = tube_cost(stateY[j])
                val = pour(stateY[i], stateY[j])
                if val:
                    seq_n_list = copy.deepcopy(seq_n["list"])
                    seq_n_list.append((i, j))
                    modified_cost_i = tube_cost(stateY[i])
                    modified_cost_j = tube_cost(stateY[j])
                    cost = stateY_cost - cost_i - cost_j + modified_cost_i + modified_cost_j
                    sequence_queue.put({
                        "cost": cost,
                        "list": seq_n_list
                    })


print("\n\nFinal State:-\n\n")
print(stateX)
# print("\n\nSequence Queue:-\n\n")
# print(sequence_queue.queue)
