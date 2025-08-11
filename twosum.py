nums = [2,7,11,15]
target = 9

# for i in  range(len(nums)):
   
#     print(nums[i])

for i in range(len(nums)):
    num1= nums[i]
    for j in range(i,len(nums)):
        num2 = nums[j]
        if num1 + num2 == target:
            output= [i , j]
            break
            
    
print(output)