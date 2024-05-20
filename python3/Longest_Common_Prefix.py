def longestCommonPrefix(strs):
    res = ""

    # Itterate over a given range of the first entry in the list 
    for index in range(len(strs[0])):
        # itterate over every word in the list
        for words in strs: 
            # If the current index is equal to the length of the word, we can end the loops. 
            # If the current index of the word is not equal to the index of the first term, we can end the loop. 
            if index == len(words) or words[index] != strs[0][index]:
                return res
        res += strs[0][index]
    return res



print(longestCommonPrefix(['']))