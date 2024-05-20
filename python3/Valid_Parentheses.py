def isValid(s): 
    # brackets = ['(','{', '[',]
    brackets = ['(', ')', '{', '}', '[', ']']
    # solution = ["()", "{}", "[]"]
    dict1 = {'(': ')', '{': '}', '[': ']'}
    # var = True

    # for index in range(0, len(s) - 1):
    #     if s[index] in dict1: 
    #         if index < s.index(dict1[s[index]]):
    #             if s[index + 1] != dict1[s[index]]: 



    hashmap = {}

    for index, value in enumerate(s): 
        hashmap[value] = index

    for i, v in hashmap: 
        print(i)
        print(v)
                

# THE index of the left most bracket < the index of the right most bracket
# Check that the index of the next item is NOT a right bracket. 
        


print(isValid("{[]}"))