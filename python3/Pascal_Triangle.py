"""

      1
    1   1 
   1  2  1
 1  3  3  1 
 .......


"""



def generate(numRows):
    #. insert to append 1 to the front of list
    #. append to the end of the list
    if numRows == 1: 
        return [[1]]

    if numRows == 2: 
        return [[1], [1, 1]]

    start = [1, 1]
    final = []
    returns = [[1], [1, 1]]

    if numRows > 2: 
        # Add all list elements between 0 and -1 val specifically 
        final.insert(0, 1)
        final.append(start[0] + start[-1])
        final.append(1)
        returns.append(final)

        # Redo this process, set final == ending 
        ending = []
        
        for i in range(0, numRows - 3):
            ending.append(1)
            for x in range(0, len(final) - 1): 
                ending.append(final[x] + final[x + 1])
            ending.append(1)
            returns.append(ending)
            final = ending 
            ending = []
    
    
       

    return returns
 # [1, 2, 1] 1 + 2, (append), 2 + 1, append


    # val [1], appends [1, 1], appends [1, 2, 1] appends  val[0], val[-1]
    # [1, 3, 3, 1] prev list append 1, adds 1 + 2, 1 + 2, append 1 
    # Adds each adjacent value within the triangle 


print(generate(5))