# def removeDuplicates(nums, val):
#     # Must itterate over array without creating new lists (Using excess memory)
#     # O(1) Time Complexity 
     
#     count = 0 

#     for i in range(len(nums)): 
#         # Itterate over each item within the list 
#         # Check if the current value of i < the value of nums (-2 to avoid indexing errors)
#         # if the current itteration is equal to the next, we continue the array. 
#         # Finally, update the array (nums[0]) = nums[i]

#         # SKIPS TO NEXT ITTERATION
#         if i < len(nums) - 2 and nums[i] == val: 
#             continue

#         #"ELSE"
#         # Update lists to point to the following itteration
#         nums[count] = nums[i]
#         count += 1
    
#     print(nums)
#     return count





#### EXAMPLE 

# class RemoveDuplicatesFromSortedArray:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # Length of the update array
#         count = 0
#         # Loop for all the elements in the array
#         for i in range(len(nums)):
#             # If the current element is equal to the next element, we skip
#             if i < len(nums) - 2 and nums[i] == nums[i + 1]:
#                 continue
#             # We will update the array in place
#             nums[count] = nums[i]
#             count += 1
#         return count


# Update pointer to put necessary list elements at the end, current list elements at the front 
# [2, 2, 3, 3] [2, 2, _, _ ] concurent list values  
# Adjust pointer

def removeElement(nums, val): 
    index = 0
    for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
    return index
        







# 2, 2, 3, 3  k=2  

print(removeElement([3, 2, 2, 3], 3))
        