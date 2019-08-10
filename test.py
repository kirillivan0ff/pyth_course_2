def birthday(iterations, ppl=60):
    from random import randrange as rand
    successCount = 0
    successRate = 0
    iterationsDone = 0
    while iterationsDone < iterations:

        successRate = 0 
        #Pattern for lists with random dates
        bDays = []
        ppl = 60    
        #random dates generator
        for x in range(ppl):
            bDays.append(str(rand(1,31)) + "." + str(rand(1,13)))

        #ppl quantity
        ppl = range(1,24)

        i = 0
            
        while i < len(ppl):
            
            match = 0
            
            for x in bDays:
                if x == bDays[i]: 
                    match += 1
                if match > 1:
                    match -= 1
                    successRate += 1
            i += 1

        iterationsDone += 1
        if successRate > 1:
            successCount += 1
    return(successCount)
