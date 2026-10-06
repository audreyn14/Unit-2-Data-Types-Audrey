""" def occupied(n,y,t):
    spaces=0
    for i in range(n):
        if y[i]=="c" and t[i]=="c":
            spaces=spaces + 1
        return spaces """


#wizard
""" def wizards (N,start,duels):
    owner=start
    changed_hands=1
    #print(duels[0][1])
    if duels[0][1]==owner:
        owner=duels[0][0]
        changed_hands=+1
    print (owner) """



def wizards (N,start,duels):
    wizards(3, "A", ["BA", "CB", "DA"])
    owner=start
    changed_hands=1
    #print(duels[0][1])
   
    if duels[0][1]==owner:
        owner=duels[0][0]
        changed_hands+=1
    print(owner,changed_hands)

    

