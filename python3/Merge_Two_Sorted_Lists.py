def mergeTwoLists(list1, list2):
    a = set()
    for i in list1: 
        a.add(i)

    for i in list2:
        a.add(i)


    return list(a)



print(mergeTwoLists([1,2,4], [1,3,4]))

