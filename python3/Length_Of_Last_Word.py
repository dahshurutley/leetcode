# def lengthOfLastWord(s):      
#     first_occurence = 0 
#     last_occurence = 0
#     counter = 0 

#     if ' ' not in s:
#         return len(s)

#     for i in range(len(s)):
#         if s[i] != ' ':
#             first_occurence = i
#             counter += 1
    
#     if counter == 1: 
#         return 1

#     for i in range(len(s[:first_occurence])):
#         if s[:first_occurence][i] == ' ':
#             last_occurence = i
    

    
#     return len(s[last_occurence + 1:first_occurence + 1])
    


def lengthOfLastWoord(s):      
    first_occurence = 0 
    last_occurence = 0
 

    if  ' ' not in s: 
        return len(s)

    for i in range(len(s)):
        if s[i] == ' ':
            last_occurence = i

    for i in range(len(s[:last_occurence])):
        if ' ' not in s[:last_occurence]:
            return len(s[:last_occurence])
        if s[:last_occurence][i] == ' ':
            first_occurence = i 

    print(s[:last_occurence])
    print(s[first_occurence])
    print(first_occurence)
    print(last_occurence)
    print(s[25])

    if s[:last_occurence] != '': 
        return len(s[first_occurence + 1:last_occurence])
    else:
        return len(s) - 1

    # return len[s[first_occurence:last_occurence]]
            
           

    
    # if len(s) <= 1 and s[0] != ' ':
    #     return 1

 

def lengthOfLastWord(s):      
    first_occurence = 0 
    last_occurence = 0
    step = 0

    if len(s) == 1 and s[0] == ' ':
        return 0

    if ' ' not in s: 
        return len(s)
 
    for i in range(len(s)): 
        if s[i] != ' ': 
            last_occurence = i

    if ' ' not in s[:last_occurence]: 
        return len(s[:last_occurence + 1])

    for i in range(len(s[:last_occurence])):
        if s[:last_occurence][i] == ' ':
            first_occurence = i
            
    
    if step != 1:
        return len(s[first_occurence + 1:last_occurence + 1]) 
    else:
        return len(s[:s.index('')])



print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("moon "))
print(lengthOfLastWord(" moon "))
print(lengthOfLastWord("moon"))
print(lengthOfLastWord("a "))

