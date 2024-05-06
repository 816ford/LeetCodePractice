nums = [1,2,3,1]

length = len(nums)
x=False
nums = sorted(nums)
i=1
while i <= length-1:
    if nums[i]==nums[i-1]:
        x=True
    i+=1
print(x)