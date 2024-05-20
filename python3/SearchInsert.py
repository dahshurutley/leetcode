def searchInsert(nums, target):


    low = 0
    high = len(nums) - 1
    mid = 0
   
    if nums[0] > target: 
        return 0
    elif nums[-1] < target: 
        return len(nums)
    
    while low <= high: 
        
        if target in nums: 
            mid = (high + low) // 2 
            if nums[mid] < target: 
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1
            else: 
                return mid 
            

        else: 
            mid = (high + low) // 2 
            if nums[mid] < target: 
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1

           
          
            if nums[low] < target < nums[mid]:
                return mid
           


print(searchInsert([1, 2 ,4, 5, 6], 3))