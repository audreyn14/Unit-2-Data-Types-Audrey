def occupied(n,y,t):
    spaces=0
    for i in range(n):
        if y[i]=="c" and t[i]=="c":
            spaces=spaces + 1
        return spaces
