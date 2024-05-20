def plusOne(digits):
    final_int = ''
    output = []

    if len(digits) < 1: 
        return [1]
    
    for i in digits: 
        final_int += str(i)

    final_int = str(int(final_int) + 1)
    for i in final_int:
        output.append(int(i))
    
    return output

print(plusOne([]))