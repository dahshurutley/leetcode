def findMedianSortedArrays(nums1, nums2):
    testing = []
    for i in nums1 : 
        testing.append(i)
    
    for i in nums2:
        testing.append(i)

    testing.sort()

    if len(testing) % 2 == 0:
        return ((testing[round(len(testing) / 2)] + testing[round((len(testing) / 2) - 1)] )/ 2)
    else: 

        while len(testing) > 1: 
            print(testing)
            for i in testing:
                if len(testing) >= 1:
                    print(testing)
                    print(i)
                    testing.remove(testing[-1]) 
                    testing.remove(i)
                

        
        
        
print(findMedianSortedArrays([], [1, 2 ,3, 4, 5, 6, 7]))
 