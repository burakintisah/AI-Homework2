import random
import copy

def print_state(state):
    print("----------")
    for row in state:
        print(row)
    print("----------")

def move(state, x, y, dir):
    if (x < 0) or (y < 0) or (x > 2) or (y > 2):
        return -1

    if dir == "up":
        if state[y - 1][x] == -1:
            state[y - 1][x] = state[y][x]
            state[y][x] = -1
            return 1
        else:
            print("Wrong move")
            return -1
    elif dir == "down":
        if state[y + 1][x] == -1:
            state[y + 1][x] = state[y][x]
            state[y][x] = -1
            return 1
        else:
            print("Wrong move")
            return -1
    elif dir == "left":
        if state[y][x - 1] == -1:
            state[y][x - 1] = state[y][x]
            state[y][x] = -1
            return 1
        else:
            print("Wrong move")
            return -1
    elif dir == "right":
        if state[y][x + 1] == -1:
            state[y][x + 1] = state[y][x]
            state[y][x] = -1
            return 1
        else:
            print("Wrong move")
            return -1


def possible_states(state):
    loc_x = 0
    loc_y = 0
    for y in range(3):
        for x in range(3):
            if state[y][x] == -1:
                loc_x = x
                loc_y = y
    x = loc_x
    y = loc_y

    new_states = []

    up_state = copy.deepcopy(state)
    down_state = copy.deepcopy(state)
    left_state = copy.deepcopy(state)
    right_state = copy.deepcopy(state)

    if move(up_state, x, y + 1, "up") != -1:
        new_states.append(up_state)

    if move(down_state, x, y - 1, "down") != -1:
        new_states.append(down_state)

    if move(left_state, x + 1, y, "left") != -1:
        new_states.append(left_state)

    if move(right_state, x - 1, y, "right") != -1:
        new_states.append(right_state)
    return new_states

def generate_state():
    state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    iter = 50

    for i in range(iter):
        new_states = possible_states(state)
        index = random.randint(0, len(new_states) - 1)
        state = new_states[index]
    return state

def h1(state):
    init_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    count = 0

    for y in range(3):
        for x in range(3):
            if init_state[y][x] != state[y][x]:
                count += 1

    return count

def h1_helper(list):
    last_state_of_path = list[len(list)-1]
    return h1(last_state_of_path)



def searchStats(state):
    queue = []
    path = []
    path.append(state)
    queue.append(path)
    while True:
        if len(queue) != 0:
            print("Start of loop.")

            print("Paths in queue:")
            for p in queue:
                print(p)
            pth = queue.pop(0)

            print("Path to extend:")
            print(pth)

            last_state = pth[len(pth) - 1]
            nxt_states = possible_states(last_state)
            new_paths = []

            print("Possible next states:")
            for st in nxt_states:
                print(st)

            for st in nxt_states:

                if st == [[1, 2, 3], [4, 5, 6], [7, 8, -1]]:
                    print("The solution is found.")
                    new_path = pth
                    new_path.append(st)
                    return new_path
                print("Checking:")
                print(st)
                if st not in pth:
                    print("Does not contain loop, extending path.")
                    # Searches whether or not that state is occurred before.
                    # If not adding it to the new paths list.
                    new_path = copy.deepcopy(pth)
                    new_path.append(st)
                    print(new_path)
                    new_paths.append(new_path)
                else:
                    print("Extension includes loop, discarded.")
            print("New paths that are obtained by extending:")

            for pt in new_paths:
                last_state = pt[len(pt) - 1]
                not_found = True
                not_found2 = True
                for q in queue:
                    if  not_found :
                        for state in q:
                            if not_found2:
                                if last_state == state:
                                    if q.index(state) > len(pt):
                                        queue.remove(q)
                                    else:
                                        new_paths.remove(pt)
                                        not_found = False
                                        not_found2 = False


            for pt in new_paths:
                print(pt)
                queue.append(pt)

            sorted(queue, key=h1_helper)

            print("End of loop, press Enter to continue.")
            #input()

        else:
            print("The solution could not found for the initial state.")
            return

init_state = [[1,2,3],[4,5,6],[7,8,-1]]

state = [[1,2,3],[4,5,6],[7,8,-1]]
move(state, 2, 1, "down")
move(state, 1, 1, "right")
print_state(state)
print("dsdsds")

state = [[1,2,3],[4,5,6],[7,8,-1]]
states = possible_states(state)
for st in states:
    print_state(st)

print("------------")
s = generate_state()
print_state( s )
print(h1(s))





searchStats(s)