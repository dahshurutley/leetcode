

def climbStairs(n): 
    # either start with two steps or one step 
    if n == 2: 
        return 2
    
    if n == 1: 
        return 1
    # CLIMBX = CLIMB X - 1 + CLIMB X-2
    return (climbStairs(n - 1) + climbStairs(n - 2))


    


def climbStairs(n): 
    # either start with two steps or one step 
    # CLIMBX = CLIMB X - 1 + CLIMB X-2

    starting_val = [1, 2]
    def climbing(n):
            # either start with two steps or one step 
        if n == 1:
            return 1 
        if n == 2: 
            return 2
        return (climbing(n - 1) + climbing(n - 2))
    starting_val.append(climbing(n))

    return starting_val[-1]
    

    

    


print(climbStairs(45))