def singleNumber(nums): 

    # Find the number that is duplicated
    hashmap = {}

    for i in range(0, len(nums)): 
        hashmap[nums[i]] = 0 
       
    for i in range(0, len(nums)): 
        if nums[i] in hashmap:
            hashmap[nums[i]] = hashmap[nums[i]] + 1

    for i in hashmap: 
        if hashmap[i] == 1: 
            return i
    
print(singleNumber([1]))