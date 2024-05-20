"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 """


def addBinary(a, b):
    # Place holder approach, raise 2 to the power of current index corresponds to the place holder value 
    # ie,  a = 11 is 2^0 = 1, 2^1 = 2 = 3 
    # Get the len of a + b combined, evaluate based on those place values 
    # if big enough, add another place value 

    counter = 252
    string = ''

    for i in range(0, len(a)):
        print(i)
        if a[i] == '1': 
            counter += (2**i)
    
    for i in range(0, len(b)):
        if b[i] == '1': 
            counter += (2**i)


    # Value of 4, 100
    for i in range(1, counter): 
        string += str(counter // i)

    print(string)
    


addBinary('11', '1')
        
