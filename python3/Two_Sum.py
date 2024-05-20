def twoSum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            print([hashmap[diff], i])
        hashmap[n] = i
      
    
a = [2, 6, 0]
for index, value in enumerate(a):
    print(f"This is the index:{index}, This is the value:{value}")
  