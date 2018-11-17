def reallocation(block):
    resultArray = []
    step = 0
    tBlock = ()
    while True:
        redistributionAmount = max(block)
        position = block.index(max(block))
        block[position] = 0
        while redistributionAmount > 0:
            try:
                block[position+1] += 1
            except:
                position = -1
                block[0] += 1
            position += 1
            redistributionAmount -= 1 
        step += 1
        tBlock = tuple(block)
        if tBlock in resultArray:
            break
        resultArray.append(tBlock)
    return step




a = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]
print(reallocation(a))
