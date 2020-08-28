# Given an array of integers, perform atmost K operations so that the sum of elements of final array is minimum. An operation is defined as follows -
# Consider any 1 element from the array, arr[i].
# Replace arr[i] by floor(arr[i]/2).
# Perform next operations on updated array.
# The task is to minimize the sum after utmost K operations.
#Operation 1 -> Select 20. Replace it by 10. New array = [10, 7, 5, 4]
# Operation 2 -> Select 10. Replace it by 5. New array = [5, 7, 5, 4].
# Operation 3 -> Select 7. Replace it by 3. New array = [5,3,5,4].
# Sum = 17.




n=int(input("Size of an array:"))
a=[]
for i in range(n):
    value=int(input("Enter value of #%d element:" %(i+1)))
    a.append(value)
k=int(input("Operation to be performed:"))

count=0
for i in range(k):
    while count<k:
        a[a.index(max(a))]=max(a) // 2 #divide max value of array of itteration by 2
        count+=1
        # print(a)
value=sum(a)
print("Minimum sum wii be:",value)
