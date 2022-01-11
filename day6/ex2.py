def min_max(a,*extraNum):
    if a>extraNum:
        maxN=a
        minN=extraNum
    else:
        minN=a
        maxN=extraNum
    return(maxN,minN)

    min_max=int (input(extraNum))

print(f'最大{maxN},最小{minN}')
