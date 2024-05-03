nums = ['2', '3', '3']

nums_dict = {}
for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1

n = len(nums)
for i in nums_dict:
    if nums_dict[i]>n/2:
        print(i)