def distance(goal):
    number = 1
    horizontal = 0
    vertical = 0
    step = 0
    while number < goal:
        step += 1
        for i in range(0,step):
            if number == goal:
                break
            horizontal += 1
            number += 1
        for i in range(0,step):
            if number == goal:
                break
            vertical += 1
            number += 1
        step += 1
        for i in range(0,step):
            if number == goal:
                break
            horizontal -= 1
            number += 1
        for i in range(0,step):
            if number == goal:
                break
            vertical -= 1
            number += 1
    result = abs(horizontal) + abs(vertical)
    return result

print(distance(361527))
