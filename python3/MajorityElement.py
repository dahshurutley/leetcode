def majorityElement(nums):

        pointer = 0
        hashmap = {}

        for i in range(0, len(nums)): 
            hashmap[nums[i]] = pointer
        

        for i in range(0, len(nums)):
            if nums[i] in hashmap: 
                hashmap[nums[i]] = hashmap[nums[i]] + 1 

        print(hashmap)
        for x in hashmap: 
            if hashmap[x] > (len(nums) / 2): 
                    return x


print(majorityElement([1]))