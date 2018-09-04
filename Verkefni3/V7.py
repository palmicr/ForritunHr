i = 1
while i <= 18:
    par_str = "Par of the hole " + str(1) + ": "
    score_str = "Score of the hole " + str(1) + ": "
    par = int(input(par_str))
    score = int(input(score_str))
    x = par - score
    if x < -3:
        print("invalid score")
    elif x == -3:
        print("albatross")
    elif x == -2:
        print("eagle")
    elif x == -1:
        print("birdie")
    elif x == 0:
        print("par")    
    elif x == 1:
        print("bogey")
    elif x == 2:
        print("double bogey")
    elif x == 3:
        print("triple bogey")
    else:
        print("bad hole")
    i += 1
