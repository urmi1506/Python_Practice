def searching():
    nums = []
    n = int(input("How many numbers do u want to enter ?"))

    print("Enter num :")
    for _ in range(n):
        num = int(input())
        nums.append(num)

    
    nums.sort()
    print("Sorted list:", nums)

    guess_num = int(input('guess no from list'))
    if guess_num in nums:
        print ("guess no in list and no is ",guess_num)
    else:
        print ("your no is not in list")

searching()