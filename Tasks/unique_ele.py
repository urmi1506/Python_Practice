# def unique_elements(nums):
#     return len(nums) == len(set(nums))

# nums = [1, 2, 3]
# print(unique_elements(nums)) 


def removeDuplicates(arr):
    if not arr:
        return []
    
    duplicates = []   
    j = 0
    
    for i in range(1, len(arr)):
        if arr[i] == arr[j]:          
            if not duplicates or duplicates[-1] != arr[i]:
                duplicates.append(arr[i])
        else:
            j += 1
            arr[j] = arr[i]
    
    return duplicates   

arr = [1, 1, 2, 2, 3, 4, 4]
print(removeDuplicates(arr))
