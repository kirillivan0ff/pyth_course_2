def montihall(iterations):
    import random

    #Success on first try
    countF = 0
    #Success on second try
    countS = 0
    n = 0

    while n < iterations:
        #Doors list
        options = ['a','b','c']
        #Correct answer
        win = random.randrange(0,3)
        winString = str(options[win])
        firstTry = random.randrange(0,3)
        
        if win == firstTry:
            countF += 1
        else:
            countS += 1
            
        n += 1

    rateF = countF*100/iterations
    rateS = countS*100/iterations

    #print(f"Number of iterations: {n}")
    #print(f"First try success rate: {rateF}%")
    #print(f"Second try success rate: {rateS}%")
    return(rateS)    
