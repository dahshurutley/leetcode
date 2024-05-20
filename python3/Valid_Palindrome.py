def isPalindrome(s):

    characters = ['(', ')', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', 
                  '|', '\\', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', ' ']

    s = s.lower()
    sinverse = s[::-1].lower()

    for i in s: 
        if i in characters:
            s = s.replace(i, '')
            sinverse = sinverse.replace(i, '')
    for i in range(0, len(s)): 
        if s[i] == sinverse[i]:
            continue
        else:
            return False 
    return True 
