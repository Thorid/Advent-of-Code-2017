def firstValue(goal):
    x = 0
    y = 0
    number = 1
    spiral = {
        (x,y) : number
        }
    step = 0
    number = 1
    while number < goal:
        step += 1
        for i in range(0,step):
            if number >= goal:
                break
            x += 1
            spiral,number = addNewNumber(x,y,spiral)
        for i in range(0,step):
            if number >= goal:
                break
            y += 1
            spiral,number = addNewNumber(x,y,spiral)
        step += 1
        for i in range(0,step):
            if number >= goal:
                break
            x -= 1
            spiral,number = addNewNumber(x,y,spiral)
        for i in range(0,step):
            if number >= goal:
                break
            y -= 1
            spiral,number = addNewNumber(x,y,spiral)
    return number

def left(x,y,spiral):
    leftNumber = spiral.get((x-1,y),0)
    return leftNumber
def leftUp(x,y,spiral):
    leftUpNumber = spiral.get((x-1,y+1),0) 
    return leftUpNumber
def up(x,y,spiral):
    upNumber = spiral.get((x,y+1),0) 
    return upNumber
def rightUp(x,y,spiral):
    rightUpNumber = spiral.get((x+1,y+1),0) 
    return rightUpNumber
def right(x,y,spiral):
    rightNumber = spiral.get((x+1,y),0)
    return rightNumber
def rightDown(x,y,spiral):
    rightDownNumber = spiral.get((x+1,y-1),0)
    return rightDownNumber
def down(x,y,spiral):
    downNumber = spiral.get((x,y-1),0)
    return downNumber
def downLeft(x,y,spiral):
    downLeftNumber = spiral.get((x-1,y-1),0)
    return downLeftNumber
def addNewNumber(x,y,spiral):
    newPosition = (x,y)
    number = left(x,y,spiral) + leftUp(x,y,spiral) + up(x,y,spiral) + rightUp(x,y,spiral) + right(x,y,spiral) + rightDown(x,y,spiral) + down(x,y,spiral) + downLeft(x,y,spiral)
    spiral[newPosition] = number
    return spiral, number
    

print(firstValue(361527))
