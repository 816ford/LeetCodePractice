
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)

    longest_series = []
    current_series = []


    x=len(nums)
    c=0
    while c < x-1:
        if nums[c]==nums[c+1]:
            nums.remove(nums[c])
            x-=1
            c-=1
        c+=1         

    for i in range(len(nums)-1):
        if nums[i+1]==nums[i]+1:
            if len(current_series)==0:
                current_series.append(nums[i])
            current_series.append(nums[i+1])
            if len(current_series)>len(longest_series):
                longest_series = current_series
        else:
            current_series = []

    if len(longest_series)==0 and nums != []:
        return 1

    return len(longest_series)



lst = [-2,5,3,2,5,6,4,3,23,2,3,34,-1,0,1,2,3,4,5]
print(longestConsecutive(lst))