# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
l1 = [2,4,3]
l2 = [5,6,4]
num1 = 0
num2 = 0
for i in range (len(l1) -1 , -1 , -1 ):
    num1 = num1*10 + l1[i]
    
for i in range (len(l2)-1 , -1 , -1):
    num2 = num2*10 + l2[i] 

sum = num1 + num2

print(sum)