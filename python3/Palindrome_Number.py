def isPalindrome(x):
    num = str(x)
    hashmap = {}
    hashmap2 = {}
    
    for i, n in enumerate(num):
        hashmap[i] = n

    for i, n in enumerate(num[::-1]): 
        hashmap2[i] = n 

    if hashmap == hashmap2:
        return True 
    else: 
        return False
   

print(isPalindrome(121))